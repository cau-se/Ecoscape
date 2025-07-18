from sink.slo_sink import SloSink
import numpy

class SliStorageSink(SloSink):

    def __init__(self, experiment_id, name, is_monitor_sink):
        super().__init__(is_monitor_sink)
        self.id = experiment_id
        self.name = name
        self.sli_values = []

    def evaluate_slo(self, value, threshold, is_bigger_better):
        self.sli_values.append(value)

    def end_hook(self):
        results = numpy.array(self.sli_values)
        numpy.savetxt(f'result/{self.id}-{self.name}.csv', results, delimiter=',')
