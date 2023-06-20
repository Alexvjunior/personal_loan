import pika
import json

class ProposalService():
    def __init__(self) -> None:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        self.channel = connection.channel()

    def publish_message(self, message:dict)->None:
        try:
            self.channel.basic_publish(
                '',
                'proposal',
                body=json.dumps(message).encode('utf-8')
            )
        except Exception as e:
            print("Erro for publish message.")