from query.query import Query
from query.query_util import value_from_prometheus_result

class QueryAccuracy(Query):

    def __init__(self, prometheus_connection):
        self.prometheus_connection = prometheus_connection

    def get_name(self):
        return f"avg(avg_over_time(accuracy[1m]))"

    def execute(self):
        result = self.prometheus_connection.custom_query(f"avg(accuracy!=0)")
        if result:
            return float(value_from_prometheus_result(result))
        else:
            return -1