import os
from celery import Celery

# Configurações do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_loan.configs.settings')
app = Celery('personal_loan')
app.config_from_object('django.conf:configs.settings', namespace='CELERY')
app.autodiscover_tasks()

@Celery.shared_task
def processar_proposta(dados_proposta):
    # Lógica de processamento da proposta
    # Pode incluir envio de e-mails, cálculos, atualizações de estado, etc.
    print(f"Processando proposta: {dados_proposta}")