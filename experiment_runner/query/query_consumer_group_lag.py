from query.query import Query


class QueryIncomingMessages(Query):

    def __init__(self, prometheus_connection, topic):
        self.topic = topic
        self.prometheus_connection = prometheus_connection

    def get_name(self):
        return f"consumer_group_lag_{self.topic}"

    def execute(self):
        result = float(self.prometheus_connection.custom_query(f"sum by(topic) (kafka_server_brokertopicmetrics_messagesin_total{{topic='{self.topic}'}})")[0]["value"][1])
        print(result)
        return result