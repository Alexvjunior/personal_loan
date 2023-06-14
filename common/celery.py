import os
from celery import Celery

# Configurações do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_loan.configs.settings')
app = Celery('common')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()