import random

from sink.slo_visualizer_sink import SloVisualizerSink

if __name__ == '__main__':
    sink = SloVisualizerSink("Hallo", False)

    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.start_new_experiment()
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)
    sink.evaluate_slo(random.randint(0, 10), 3, True)