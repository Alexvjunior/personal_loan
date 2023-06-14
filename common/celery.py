import os
from celery import Celery, shared_task

# Configurações do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_loan.configs.settings')
app = Celery('personal_loan.common')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def processar_proposta(dados_proposta):
    # Lógica de processamento da proposta
    # Pode incluir envio de e-mails, cálculos, atualizações de estado, etc.
    print(f"Processando proposta: {dados_proposta}")