# RabbitMQ Message Queue

Este projeto é um simples caso de uso do [RabbitMQ](https://www.rabbitmq.com/) e [Pika](https://pika.readthedocs.io/en/stable/) para enviar e receber mensagens em uma fila com Python.

## Configuração

Antes de executar os scripts, certifique-se de executar o RabbitMQ. Para isso, você pode usar o docker-compose existente na raiz do projeto.

## Instalação

1. Clone este repositório:

   ```shell
   git clone https://github.com/eliedsonholanda/rabbitmq-message-queue.git
   ```

2. Acesse o diretório:
    ```shell
    cd rabbitmq-message-queue
    ```

3. Instale as dependências:
    ```shell
    pip install -r requirements.txt
    ```

## Uso
### Recebendo mensagens
Para receber mensagens da fila, execute o script `receiver.py`:
```shell
python receiver.py
```
_As mensagens recebidas serão exibidas no terminal._

### Enviando mensagens
Em um novo terminal, execute o script `sender.py`:
```shell
python sender.py
```
_Siga as instruções no terminal para digitar a mensagem que deseja enviar._

### Encerrando a Aplicação
Para encerrar a aplicação em qualquer momento, pressione CTRL+C.

