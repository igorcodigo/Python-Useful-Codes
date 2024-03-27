import os
import python_minifier

def minify_python_directory(input_directory, output_directory=None):
    # Garantir que o diretório de saída existe mas não tem 
    if output_directory and not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Listar todos os arquivos no diretório de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith('.py'):
            input_file_path = os.path.join(input_directory, filename)
            
            # Construir o caminho do arquivo de saída
            if output_directory:
                output_file_path = os.path.join(output_directory, filename)
            else:
                # Adiciona um sufixo ao arquivo original para salvar a versão minificada
                output_file_path = os.path.join(input_directory, filename.replace('.py', '_min.py'))
            
            # Minificar o arquivo
            minify_python_file(input_file_path, output_file_path)

def minify_python_file(input_file_path, output_file_path):
    # Ler o código-fonte do arquivo de entrada
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        source_code = input_file.read()

    # Minificar o código-fonte
    minified_code = python_minifier.minify(source_code, remove_annotations=True, remove_pass=True, rename_locals=True)

    # Escrever o código minificado no arquivo de saída
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(minified_code)

# Obter o caminho do diretório atual onde o script está localizado
current_directory = os.path.abspath(os.path.dirname(__file__))


# Exemplo de uso
input_directory = current_directory
output_directory = r'Pasta_Minificada'
minify_python_directory(input_directory, output_directory)
