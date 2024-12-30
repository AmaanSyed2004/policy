from confluent_kafka import Producer
import os
import json
def produce_event(topic, event):
    kafka_server = os.getenv('KAFKA_BOOTSTRAP_SERVER')
    if not kafka_server:
        print("KAFKA_BOOTSTRAP_SERVER environment variable is not set.")
    
    producer = Producer({'bootstrap.servers': kafka_server})

    producer.produce(topic, json.dumps(event))
    producer.flush()
    print(f"Message sent-> {topic}: {event}")
