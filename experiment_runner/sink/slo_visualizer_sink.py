import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

from sink.slo_sink import SloSink

class SloVisualizerSink(SloSink):

    def __init__(self, name, is_monitor_sink):
        super().__init__(is_monitor_sink)
        fig, ax = plt.subplots(1, 1)
        self.fig = fig
        self.name = name
        self.fig.canvas.manager.set_window_title(name)
        self.ax = ax
        self.i = 0
        self.x = []
        self.y = []
        self.y2 = []
        self.y3 = []
        self.active_y = self.y
        self.color = 'b'
        self.linestyle = ':'

    def start_new_experiment(self):
        self.active_y = self.y3
        self.y2 = []
        self.i = 0
        self.x = []
        self.color = 'g'
        self.linestyle = '--'

    def evaluate_slo(self, value, threshold, is_bigger_better):
        self.x.append(self.i)
        self.active_y.append(value)
        self.y2.append(threshold)
        self.ax.plot(self.x, self.active_y, linestyle=self.linestyle, color=self.color)
        self.ax.plot(self.x, self.y2, color='r')

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(1)
        self.i += 1

    def is_monitor_sink(self):
        return super().is_monitor_sink()

    def end_hook(self):
        self.fig.savefig(f"result/{self.name}-plot.png")
