import os
from pdfminer.high_level import extract_text

# Caminho da pasta com os PDFs
dir_pdfs = os.path.join(os.getcwd(), 'pdfs')

# Garante que a pasta existe
os.makedirs(dir_pdfs, exist_ok=True)

# Lista todos os arquivos PDF na pasta
docs_pdf = [f for f in os.listdir(dir_pdfs) if f.lower().endswith('.pdf')]

if not docs_pdf:
    print('Nenhum PDF encontrado na pasta pdfs.')
else:
    for pdf in docs_pdf:
        caminho_pdf = os.path.join(dir_pdfs, pdf)
        texto = extract_text(caminho_pdf)
        nome_txt = os.path.splitext(pdf)[0] + '.txt'
        caminho_txt = os.path.join(dir_pdfs, nome_txt)
        with open(caminho_txt, 'w', encoding='utf-8') as f:
            f.write(texto)
        print(f'Convertido: {pdf} -> {nome_txt}')
        try:
            os.remove(caminho_pdf)
            print(f'PDF removido: {pdf}')
        except Exception as e:
            print(f'Erro ao remover {pdf}: {e}')
print('Conversão e remoção finalizadas.')
