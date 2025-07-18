from sink.slo_sink import SloSink

class SloViolationScoreSink(SloSink):

    def __init__(self, is_monitor_sink):
        super().__init__(is_monitor_sink)
        self.score: float = 0.0
        self.score_count = 0

    def evaluate_slo(self, value, threshold, is_bigger_better) -> bool:
        self.score_count = self.score_count + 1
        if is_bigger_better:
            if value < threshold:
                violation_score = 1 - (value / threshold)
                self.score = self.score + violation_score
        else:
            if value > threshold:
                violation_score = 1 - (threshold / value)
                self.score = self.score + violation_score
        return True

    def is_monitor_sink(self):
        return super().is_monitor_sink()

    def get_score(self) -> float:
        return self.score / self.score_count

    def end_hook(self):
        print(self.get_score())

