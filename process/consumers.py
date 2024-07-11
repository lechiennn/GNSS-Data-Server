from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json
from process.serializers import DataSerializer
from rest_framework.exceptions import ValidationError

class Consumer:
    def __init__(self, 
                topics,
                bootstrap_servers='localhost:9092',
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))):
        
        self.consumer = KafkaConsumer(
            topics,
            bootstrap_servers=bootstrap_servers, 
            auto_offset_reset='latest',  # Read from the earliest offset
            enable_auto_commit=False,
            group_id="1",
            value_deserializer=value_deserializer)
    
    def consume_data(self):
        for message in self.consumer:
            try:
                self.process_message(message.value)
                self.consumer.commit()
            except ValidationError as e:
                print(e)
            except KafkaError as e:
                print(f"Commit failed: {e}")

    def process_message(self, message):
        serializer = DataSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(message)
