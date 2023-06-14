import os
from celery import Celery
from django.conf import settings

# Configurações do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_loan.configs.settings')
app = Celery('personal_loan.common')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)