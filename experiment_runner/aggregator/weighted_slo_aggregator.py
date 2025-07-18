from typing import List

from sink.slo_violation_score_sink import SloViolationScoreSink

class WeightedSloAggregator:

    def __init__(self, slo_sinks: List[SloViolationScoreSink], weights: List[float]):
        if len(slo_sinks) != len(weights):
            raise Exception("Slos and weights should have the same length")
        if abs(sum(weights) - 1) > 0.001:
            raise Exception("Weights should sum up to 1")

        self.slo_sinks: List[SloViolationScoreSink] = slo_sinks
        self.weights: List[float] = weights

    def get_aggregated_score(self):
        total_score = 0.0
        for i in range(len(self.slo_sinks)):
            total_score = total_score + (self.slo_sinks[i].get_score() * self.weights[i])
        return total_score