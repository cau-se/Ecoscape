import string
import random

import yaml
from prometheus_api_client import PrometheusConnect

from config.experiment_directory_parser import ExperimentDirectoryParser

from config.experiment_duration_parser import ExperimentDurationParser
from ecoscape_core import EcoscapeCore

from query.generic_query import GenericQuery
from scenario import SLO
from sink.sli_storage_sink import SliStorageSink
from sink.slo_value_printer_sink import SloValuePrinterSink
from sink.slo_violation_score_sink import SloViolationScoreSink

def arg_or_default(arg, default):
    if arg:
        return arg
    return default

def generate_id(length=5):
    characters = string.ascii_lowercase
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id


if __name__ == '__main__':
    print("Started")
    with open("experiment_config/experiment_duration.yaml") as file:
        experiment_duration_config = yaml.safe_load(file)

    with open("experiment_config/experiment_directory.yaml") as file:
        experiment_directory_config = yaml.safe_load(file)

    with open("experiment_config/slos.yaml") as file:
        slo_config = yaml.safe_load(file)

    experiment_id = generate_id()
    print(f"Running experiment with id {experiment_id}")
    slo_sinks_dict = dict()

    prometheus_connection = PrometheusConnect(slo_config["prometheus"]["url"])

    for slo_config in slo_config["slos"]:
        slo_name = slo_config["name"]
        slo = SLO(
            GenericQuery(
                prometheus_connection=prometheus_connection,
                name=slo_name,
                query=slo_config["query"]),
            slo_config["threshold"],
            slo_config["isBiggerBetter"]
        )

        slo_sinks_dict[slo] = {
            "score": SloViolationScoreSink(is_monitor_sink=False),
            "print": SloValuePrinterSink(slo_name, True),
            "store": SliStorageSink(experiment_id, slo_name, True)
        }

    EcoscapeCore(
        experiment_duration_config=ExperimentDurationParser().parse(experiment_duration_config),
        experiment_directory_config=ExperimentDirectoryParser().parse(experiment_directory_config),
        slo_sinks=slo_sinks_dict
    ).run()
