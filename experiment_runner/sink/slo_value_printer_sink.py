from sink.slo_sink import SloSink

class SloValuePrinterSink(SloSink):

    def __init__(self, name, is_monitor_sink):
        super().__init__(is_monitor_sink)
        self.name: str = name

    def evaluate_slo(self, value, threshold, is_bigger_better):
        print(f"{self.name}: {value}")

    def is_monitor_sink(self):
        return super().is_monitor_sink()

    def end_hook(self):
        pass



