"""
WSGI config for processServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from process.consumers import Consumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'processServer.settings')

application = get_wsgi_application()

# # consumer = Consumer(**settings.KAFKA_SETTINGS)
# consumer = Consumer(
#     topics='gnss',
#     bootstrap_servers='localhost:9092'
# )
# consumer.consume_data()