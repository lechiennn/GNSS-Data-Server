from django.core.management.base import BaseCommand
from django.conf import settings

from process.consumers import Consumer

import json

class Command(BaseCommand):
    help = 'Consumes messages from Kafka topic'

    def handle(self, *args, **kwargs):
        consumer = Consumer(**settings.KAFKA_SETTINGS)
        consumer.consume_data()
