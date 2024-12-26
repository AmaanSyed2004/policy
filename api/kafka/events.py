from confluent_kafka.admin import AdminClient, NewTopic
import os


def create_topics():
    kafka_server = os.getenv('KAFKA_BOOTSTRAP_SERVER')
    if not kafka_server:
        print("KAFKA_BOOTSTRAP_SERVER environment variable is not set.")

    print(f"Connecting to Kafka server at {kafka_server}")
    
    admin_client = AdminClient({'bootstrap.servers': kafka_server})

    required_topics= ['policy-created', 'policy-updated', 'policy-deleted']
    existing_topics= admin_client.list_topics().topics.keys()

    topics_to_create= [
        NewTopic(topic, num_partitions=1, replication_factor=1) 
        for topic in required_topics
        if topic not in existing_topics
        ]
    if not topics_to_create:
        print("All required topics already exist")
        return
    try:
        futures = admin_client.create_topics(topics_to_create)
        for topic, future in futures.items():
            try:
                future.result()  
                print(f"Topic {topic} created")
            except Exception as e:
                print("Error:")
                print(f"Failed to create topic {topic}: {e}")
    except Exception as e:
        print(f"Failed to create topics: {e}")
