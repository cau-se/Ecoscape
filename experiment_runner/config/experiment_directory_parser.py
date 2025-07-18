from config.directory_config import ExperimentDirectoryConfig


class ExperimentDirectoryParser:

    def parse(self, config):
        return ExperimentDirectoryConfig(
            infra_dir=config["infra"],
            sut_dir=config["sut"],
            chaos_dir=config["chaos"],
            load_dir=config["load"],
            monitor_dir=config["monitor"]
        )
