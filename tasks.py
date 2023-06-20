import json
import os
from random import randint

import pika
import requests

RABBIT_HOST = os.environ.get("RABBIT_HOST", "localhost")
WEB_HOST = os.environ.get("WEB_HOST", "localhost")

# Configurações de conexão com o RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(f'{RABBIT_HOST}', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='proposal', durable=True)


# Função que será executada quando uma mensagem for recebida
def callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body.decode('utf-8')}")
    choice = 'Reject' if randint(0, 1) else 'Approved'
    message = json.loads(body.decode('utf-8'))
    try:
        response = requests.patch(
            f'http://{WEB_HOST}:8000/proposal/{message["id"]}/', {"status": choice}
            )
        print(f"Mensagem Processada com sucesso: {response}")
    except Exception as e:
        print(f'Problems to update proposal: {e}')


# Configuração do consumidor
channel.basic_consume(
    queue='proposal', on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens...')
# Inicia a leitura de mensagens
channel.start_consuming()
