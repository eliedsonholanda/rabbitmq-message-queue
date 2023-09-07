import pika

class MessageQueue:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = self.establish_connection()
        self.channel = self.setup_channel()

    def establish_connection(self):
        connection_params = pika.ConnectionParameters('localhost')
        return pika.BlockingConnection(connection_params)

    def setup_channel(self):
        channel = self.connection.channel()
        channel.queue_declare(queue=self.queue_name)
        channel.basic_qos(prefetch_count=1)
        return channel

    def send_message(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
        print(f"Mensagem '{message}' enviada com sucesso!")

    def receive_messages(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self._process_message)
        print('Aguardando mensagens. Para sair, pressione CTRL+C')
        self.channel.start_consuming()

    def _process_message(self, ch, method, properties, body):
        message = body.decode()
        print("Mensagem recebida:", message)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def close_connection(self):
        if self.connection.is_open:
            self.connection.close()
