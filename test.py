#!/usr/bin/env python3
from kafka.admin import KafkaAdminClient

def list_kafka_topics(bootstrap_servers):
    try:
        # Create an admin client
        admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
        
        # Get list of topics
        topics = admin_client.list_topics()
        
        # Print topics
        print("Kafka Topics:")
        for topic in topics:
            print(topic)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with your Kafka broker address
    bootstrap_servers = ['localhost:9092']
    
    list_kafka_topics(bootstrap_servers)