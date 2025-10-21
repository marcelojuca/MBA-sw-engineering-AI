import threading
import time
from search import search_prompt

def show_processing_indicator(stop_event):
    # """Show a processing indicator while the search is running (uv style)"""
    # indicators = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    # i = 0
    # while not stop_event.is_set():
    #     print(f"\rRESPOSTA: Processando {indicators[i % len(indicators)]}", end="", flush=True)
    #     i += 1
    #     time.sleep(0.1)
    print("\rRESPOSTA: ", end="", flush=True)  # Clear the processing and show "RESPOSTA: " ready for answer
    pass

def main():
    print("=== Chat de Busca Semântica ===")
    print("Digite 'sair' ou 'quit' para encerrar o chat.")
    print("=" * 50)
    
    # Initialize the search chain
    try:
        chain = search_prompt()
        if not chain:
            print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
            return
    except Exception as e:
        print(f"Erro ao inicializar o chat: {e}")
        print("Verifique se o banco de dados está rodando e as variáveis de ambiente estão configuradas.")
        return
    
    # Interactive chat loop
    while True:
        try:
            # Get user input
            question = input("\nFaça sua pergunta: ").strip()
            
            # Check for exit commands
            if question.lower() in ['sair', 'quit', 'exit', 'q']:
                print("\nEncerrando o chat. Até logo!")
                break
            
            # Skip empty questions
            if not question:
                print("Por favor, digite uma pergunta válida.")
                continue
            
            # Process the question
            print(f"\nPERGUNTA: {question}")
            
            # Start processing indicator
            stop_event = threading.Event()
            processing_thread = threading.Thread(target=show_processing_indicator, args=(stop_event,))
            processing_thread.daemon = True
            processing_thread.start()
            
            try:
                # Get response from the chain
                response = chain.invoke(question)
                
                # Stop the processing indicator
                stop_event.set()
                processing_thread.join(timeout=0.1)
                
                # Display the response (on the same line after "RESPOSTA: ")
                print(response.content)
                
            except Exception as e:
                # Stop the processing indicator
                stop_event.set()
                processing_thread.join(timeout=0.1)
                raise e

        except KeyboardInterrupt:
            print("\n\nEncerrando o chat. Até logo!")
            break
        except Exception as e:
            print(f"\nErro ao processar a pergunta: {e}")
            print("Tente novamente ou digite 'sair' para encerrar.")

if __name__ == "__main__":
    main()