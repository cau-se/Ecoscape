from query.query import Query
from query.query_util import value_from_prometheus_result

class GenericQuery(Query):

    def __init__(self, prometheus_connection, name, query):
        self.prometheus_connection = prometheus_connection
        self.name = name
        self.query = query

    def get_name(self):
        return self.name

    def execute(self):
        result = self.prometheus_connection.custom_query(self.query)
        if result:
            return float(value_from_prometheus_result(result))
        else:
            return -1