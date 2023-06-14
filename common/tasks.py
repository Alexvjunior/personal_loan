from celery import shared_task

@shared_task
def processar_proposta(dados_proposta):
    # Lógica de processamento da proposta
    # Pode incluir envio de e-mails, cálculos, atualizações de estado, etc.
    print(f"Processando proposta: {dados_proposta}")