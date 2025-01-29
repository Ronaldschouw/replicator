#!/usr/bin/env python3
from kafka import KafkaAdminClient, KafkaConsumer
from kafka.admin import NewTopic
from kafka.errors import KafkaError
from kafka import KafkaConsumer, TopicPartition
from kafka import KafkaAdminClient
import os
import logging

# Configure logging
# logging.basicConfig(level=logging.DEBUG)

def get_kafka_topics():
    bootstrap_servers = '127.0.0.1:9092' # Replace with your Kafka broker address
    security_protocol = 'PLAINTEXT' # Replace with your security protocol

    try:
        admin_client = KafkaAdminClient(
            bootstrap_servers=bootstrap_servers,
            security_protocol=security_protocol
        )
        topics = admin_client.list_topics()
        print("Kafka Topics:")
        for topic in topics:
            print(topic)
    except KafkaError as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    get_kafka_topics()