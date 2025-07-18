from config.duration_config import ExperimentDurationConfig

class ExperimentDurationParser:

    def parse(self, config):
        return ExperimentDurationConfig(
            duration=config["duration"],
            eval_delay=config["evalDelay"],
            load_delay=config["loadDelay"],
            repetitions=config["repetitions"],
            chaos_delay=config["chaosDelay"]
        )
