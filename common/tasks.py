from celery import shared_task, current_task
from kombu import Queue

@shared_task
def sua_tarefa():
    # Obtenha a fila do RabbitMQ
    queue = current_task.get_queue()
    print("funcionando")

    # Configure a fila para receber mensagens
    with queue.Consumer() as consumer:
        # Itere sobre as mensagens recebidas
        for message in consumer:
            # Acesse os dados da mensagem
            payload = message.payload

            # Execute a lógica desejada com os dados da mensagem
            print(payload)

            # Marque a mensagem como concluída
            message.ack()

    return 2