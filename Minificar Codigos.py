import python_minifier

def minify_python_file(input_file_path, output_file_path):
    # Ler o código-fonte do arquivo de entrada
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        source_code = input_file.read()

    # Minificar o código-fonte
    minified_code = python_minifier.minify(source_code, remove_annotations=True, remove_pass=True, rename_locals=True)

    # Escrever o código minificado no arquivo de saída
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(minified_code)

# Coloque aqui o caminho do arquivo de entrada e o caminho/nome no qual o arquivo será salvo
        
input_file_path = r'Minificar Codigos.py'
output_file_path = r'Exemplo\Minificado_Minificar Codigos.py'
minify_python_file(input_file_path, output_file_path)
