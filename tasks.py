import os
from celery import Celery
from kombu import Queue
from random import randint
import requests

# Defina a configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

# Crie a instância do aplicativo Celery
app = Celery('tasks')

# Configuração do RabbitMQ
app.conf.broker_url = 'amqp://guest:guest@rabbitmq:5672/'

CELERY_QUEUES = (
    Queue('proposal', routing_key='proposal'),
)

app.conf.task_queues = CELERY_QUEUES

# Carregue as configurações do Celery a partir das configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover das tarefas do Celery no seu projeto
app.autodiscover_tasks()


@app.task(queue='proposal')
def update_proposal(message):
    print("updated")
