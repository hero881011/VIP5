#!/usr/bin/env python
# coding:utf-8

# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime
from pymysqlreplication import BinLogStreamReader
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from pymysqlreplication.row_event import (DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent, )


class Kafka_producer():

    def __init__(self, kafkahost, kafkaport, kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkaTopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers='{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort))

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            producer.send(self.kafkaTopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print(e)


class Kafka_consumer():

    def __init__(self, kafkahost, kafkaport, kafkatopic, groupid):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkaTopic = kafkatopic
        self.groupId = groupid
        self.consumer = KafkaConsumer(self.kafkaTopic, group_id=self.groupId,
                                      bootstrap_servers='{kafka_host}:{kafka_port}'.format(
                                          kafka_host=self.kafkaHost,
                                          kafka_port=self.kafkaPort
                                      ))

    def consume_date(self):
        try:
            for message in self.consumer:
                yield message
        except KeyboardInterrupt as e:
            print(e)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


# for binlogevent in stream:
#   binlogevent.dump()
# stream.close()
def main():
    producer = Kafka_producer("10.40.58.114", 9092, "tmysql")
    mysql_settings = {'host': '10.40.63.52', 'port': 3306, 'user': 'repl_user', 'passwd': 'zaq1xsw2'}
    stream = BinLogStreamReader(connection_settings=mysql_settings, server_id=7765,
                                only_schemas=["test"],
                                only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent],
                                resume_stream=True,
                                blocking=True)

    for binlogevent in stream:
        for row in binlogevent.rows:
            event = {"schema": binlogevent.schema, "table": binlogevent.table,
                     "log_pos": binlogevent.packet.log_pos}
            if isinstance(binlogevent, DeleteRowsEvent):
                event["action"] = "delete"
                event["values"] = dict(row["values"].items())
                event = dict(event.items())
            elif isinstance(binlogevent, UpdateRowsEvent):
                event["action"] = "update"
                event["before_values"] = dict(row["before_values"].items())
                event["after_values"] = dict(row["after_values"].items())
                event = dict(event.items())
            elif isinstance(binlogevent, WriteRowsEvent):
                event["action"] = "insert"
                event["values"] = dict(row["values"].items())
                event = dict(event.items())
            print(json.dumps(event, cls=DateEncoder))
            producer.sendjsondata(json.dumps(event, cls=DateEncoder))
            sys.stdout.flush()

    stream.close()


if __name__ == "__main__":
    main()
