from pdfminer.high_level import extract_text

def verificar_informacao_no_pdf(caminho_do_pdf, informacao):
    try:
        # Extrair o texto do PDF
        texto = extract_text(caminho_do_pdf)
        # Verificar se a informação está no texto
        
        return informacao in texto
    except Exception as e:
        print(f"Ocorreu um erro na funcao verificar_informacao_no_pdf: {e}")
        return False

# Caminho do arquivo PDF
caminho_do_pdf = r'C:'

# Informação a ser procurada
cpf_a_ser_procurado = "009.008.007-06"

# Chamando a função e imprimindo o resultado
resultado = verificar_informacao_no_pdf(caminho_do_pdf, cpf_a_ser_procurado)
print("Informação encontrada:" if resultado else "Informação não encontrada.")
