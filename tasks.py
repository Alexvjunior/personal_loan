import os
from celery import Celery

# Defina a configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

# Crie a instância do aplicativo Celery
app = Celery('tasks')

# Configuração do RabbitMQ
app.conf.broker_url = 'amqp://guest:guest@localhost:5672/'

# Carregue as configurações do Celery a partir das configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover das tarefas do Celery no seu projeto
app.autodiscover_tasks()