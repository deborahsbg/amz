import os
try:
    from pdfminer.high_level import extract_text
except ImportError:
    print('pdfminer.six não está instalado. Instale com: pip install pdfminer.six')
    exit(1)
try:
    from PIL import Image
except ImportError:
    print('Pillow não está instalado. Instale com: pip install pillow')
    exit(1)
try:
    import pytesseract
except ImportError:
    print('pytesseract não está instalado. Instale com: pip install pytesseract')
    exit(1)

# Caminho da pasta com os PDFs
dir_pdfs = os.path.join(os.getcwd(), 'pdfs')

# Garante que a pasta existe
os.makedirs(dir_pdfs, exist_ok=True)

# Extensões suportadas
extensoes_pdf = ['.pdf']
extensoes_img = ['.jpg', '.jpeg', '.png']

arquivos = [f for f in os.listdir(dir_pdfs) if os.path.splitext(f)[1].lower() in extensoes_pdf + extensoes_img]

if not arquivos:
    print('Nenhum arquivo encontrado na pasta pdfs.')
else:
    for arquivo in arquivos:
        caminho = os.path.join(dir_pdfs, arquivo)
        nome_txt = os.path.splitext(arquivo)[0] + '.txt'
        caminho_txt = os.path.join(dir_pdfs, nome_txt)
        ext = os.path.splitext(arquivo)[1].lower()
        try:
            if ext in extensoes_pdf:
                texto = extract_text(caminho)
                with open(caminho_txt, 'w', encoding='utf-8') as f:
                    f.write(texto)
                os.remove(caminho)  # Remove o PDF após conversão
                print(f'PDF convertido: {arquivo}')
            elif ext in extensoes_img:
                img = Image.open(caminho)
                texto = pytesseract.image_to_string(img, lang='por')
                with open(caminho_txt, 'w', encoding='utf-8') as f:
                    f.write(texto)
                print(f'Imagem convertida: {arquivo}')
        except Exception as e:
            print(f'Erro ao converter {arquivo}: {e}')
    print('Conversão finalizada.')
