from argparse import ArgumentParser


class ConfigurationArgumentParser:

    def __init__(self):
        self.argument_parser = ArgumentParser(description="Ecoscape")
        self.argument_parser.add_argument("--duration", type=int, help="experiment duration")
        self.argument_parser.add_argument("--load_delay", type=int, nargs='?', help="delay until the load generator starts")
        self.argument_parser.add_argument("--eval_delay", type=int, nargs='?',
                                 help="delay until the evaluation of the slo starts")
        self.argument_parser.add_argument("--repetitions", type=int, nargs='?', help="number of experiment runs")

        self.argument_parser.add_argument("--dir_load", type=str, default="load/base", nargs='?',
                                 help="directory of the load specification")
        self.argument_parser.add_argument("--dir_sut", type=str, default="sut/base", nargs='?',
                                 help="directory of the sut specification")
        self.argument_parser.add_argument("--dir_sut_patch", type=str, default="sut/patch", nargs='?',
                                 help="directory of the patched sut specification")
        self.argument_parser.add_argument("--dir_infra", type=str, default="infra/base", nargs='?',
                                 help="directory of the infrastructure specification")
        self.argument_parser.add_argument("--dir_infra_patch", type=str, default="infra/patch", nargs='?',
                                 help="directory of the patched (chaotic) infrastructure specification")
        self.argument_parser.add_argument("--dir_monitor", type=str, default="monitor", nargs='?',
                                 help="directory of the monitor specification")

        args = self.argument_parser.parse_args()