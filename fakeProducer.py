from kafka import KafkaProducer
from faker import Faker
from environs import Env
import json
import time
from datetime import datetime, timezone

env = Env()
env.read_env('dev.env')

# Initialize Faker and KafkaProducer
fake = Faker()
Faker.seed(0)

producer = KafkaProducer(
    bootstrap_servers=env("BOOTSTRAP_SERVERS", str, "localhost:9092"),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_fake_data():
    # Generate a dictionary of fake data
    return {
        'station': env("STATION", str, ""),
        'temperature': fake.pyfloat(right_digits=2, min_value=10, max_value=40),
        'precipitation': fake.pyfloat(right_digits=2, min_value=0, max_value=200),
        'created_at': datetime.now(timezone.utc).isoformat()
    }

def send_data_to_kafka(topic, data):
    producer.send(topic, data)
    producer.flush()

if __name__ == "__main__":
    topic_name = 'gnss'
    
    while True:
        data = generate_fake_data()
        send_data_to_kafka(topic_name, data)
        print(f"Sent: {data}")
        
        # Wait for 1 second before sending the next message
        time.sleep(1)