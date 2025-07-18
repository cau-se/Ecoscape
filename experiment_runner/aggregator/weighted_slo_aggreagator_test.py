from aggregator.weighted_slo_aggregator import WeightedSloAggregator
from sink.slo_sink import SloSink
from slo import SLO


class MockSloSink(SloSink):

    def __init__(self, score):
        self.score = score

    def get_score(self) -> float:
        return self.score

    def evaluate_slo(self, slo: SLO):
        pass


class WeightedSloAggreagtorTest:

    def __init__(self):
        self.testee = WeightedSloAggregator([MockSloSink(0.4), MockSloSink(0.0)], [0.3333, 0.6666])

    def test(self):
        print(self.testee.get_aggregated_score())

if __name__ == '__main__':
    WeightedSloAggreagtorTest().test()