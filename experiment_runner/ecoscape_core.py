import random
import string
import time
from typing import Dict, List

from aggregator.weighted_slo_aggregator import WeightedSloAggregator
from config.directory_config import ExperimentDirectoryConfig
from config.duration_config import ExperimentDurationConfig
from ecoscape_client import EcoscapeClient
from ecoscape_client_mode_aware import EcoscapeClientModeAware
from mode.mode import ModeFullExperimentRun
from scenario import Scenario, SLO
from sink.slo_sink import SloSink

class EcoscapeCore:
    def __init__(
            self,
            experiment_duration_config: ExperimentDurationConfig,
            experiment_directory_config: ExperimentDirectoryConfig,
            slo_sinks: Dict[SLO, Dict[string, SloSink]]
    ):
        self.ecoscape_client = EcoscapeClient(
            "build",
            experiment_directory_config
        )
        self.slo_sinks = slo_sinks
        self.duration_config = experiment_duration_config

    def run(self):
        experiment_id = self.generate_id()
        print(f"Running experiment with id {experiment_id}")
        repetitions = self.duration_config.repetitions

        Scenario(
            slo_sinks=self.slo_sinks,
            ecoscape_client=EcoscapeClientModeAware(
                mode=ModeFullExperimentRun(),
                load_generation_delay=self.duration_config.load_delay,
                infra_delay=0.5 * self.duration_config.load_delay,
                ecoscape_client=self.ecoscape_client,
            ),
            duration=self.duration_config.duration,
            evaluation_delay=self.duration_config.eval_delay,
            chaos_delay=self.duration_config.chaos_delay
        ).run()
        for i in range(repetitions):
            print("Wait to start new exeriment")
            if i < repetitions - 1:
                time.sleep(60)

        score_sinks = []
        for slo in self.slo_sinks:
            for sink_name in self.slo_sinks[slo]:
                if sink_name == "score":
                    score_sinks.append(self.slo_sinks[slo][sink_name])

        for score_sink in score_sinks:
            print(score_sink.get_score())

        aggregator = WeightedSloAggregator(score_sinks, [0.5, 0.25, 0.25])
        print("Ecoscape score: ", aggregator.get_aggregated_score())

    def generate_id(self, length=5):
        characters = string.ascii_lowercase
        random_id = ''.join(random.choice(characters) for _ in range(length))
        return random_id