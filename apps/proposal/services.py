import json

import pika


class ProposalService():
    def __init__(self) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq'))
        self.channel = connection.channel()

    def publish_message(self, message: dict) -> None:
        m = {
            'id': message['id']
        }
        try:
            self.channel.basic_publish(
                '',
                'proposal',
                body=json.dumps(m).encode('utf-8')
            )
        except Exception as e:
            print(f"Erro for publish message. {e}")
