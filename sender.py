from message_queue import MessageQueue

def main():
    queue_name = 'queue_test'
    message_queue = MessageQueue(queue_name)
    
    try:
        while True:
            message = input("Digite a mensagem a ser enviada (ou CTRL+C para sair): ")
            message_queue.send_message(message)
    except KeyboardInterrupt:
        print("Encerrando a aplicação...")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
    finally:
        message_queue.close_connection()

if __name__ == "__main__":
    main()
