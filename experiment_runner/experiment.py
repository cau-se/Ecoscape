import sys
from time import sleep

from prometheus_api_client import PrometheusConnect
from query.query import Query


class Experiment:

    def __init__(self, url, prometheus_query):
        self.prometheus_connection = PrometheusConnect(url=url)
        self.prometheus_query: Query = prometheus_query

    def execute_continuously(self, duration=60, interval=1):
        print(self.prometheus_query.get_name())
        for i in range(duration):
            try:
                print(self.prometheus_query.execute())
                sleep(interval)
            except KeyboardInterrupt:
                print('Ended by user')
                sys.exit(0)
