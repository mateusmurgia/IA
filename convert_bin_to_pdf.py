import os

def bin_to_pdf(input_file, output_file):
    """
    Converte um arquivo .bin para .pdf copiando os dados brutos.
    Nota: Isso só funciona se o arquivo .bin já estiver em formato PDF.
    """
    try:
        # Verifica se o arquivo de entrada existe
        if not os.path.exists(input_file):
            print(f"Erro: Arquivo de entrada '{input_file}' não encontrado.")
            return False
        
        # Lê o conteúdo binário
        with open(input_file, 'rb') as bin_file:
            bin_data = bin_file.read()
        
        # Escreve o mesmo conteúdo com extensão .pdf
        with open(output_file, 'wb') as pdf_file:
            pdf_file.write(bin_data)
        
        print(f"Arquivo convertido com sucesso: {output_file}")
        return True
    
    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")
        return False

# Exemplo de uso
if __name__ == "__main__":
    while True:
        input_path = input("Digite o caminho do arquivo .bin (ou 'sair' para encerrar): ")
        
        if input_path.lower() == 'sair':
            print("Encerrando o programa...")
            break
            
        output_path = input_path.rsplit('.', 1)[0] + '.pdf'
        
        bin_to_pdf(input_path, output_path)
        
        # Pergunta se deseja converter outro arquivo
        continuar = input("Deseja converter outro arquivo? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando o programa...")
            break
