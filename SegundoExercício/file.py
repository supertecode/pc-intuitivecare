import pdfplumber
import pandas as pd
import zipfile

# Nome do arquivo PDF (Anexo I)
pdf_file = "Anexo_I.pdf"

# Lista para armazenar os dados
data = []

# Abre o PDF
with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        tables = page.extract_table()  # Tenta extrair tabela da página
        if tables:
            data.extend(tables)  # Adiciona os dados extraídos à lista
            
# Converte os dados para um DataFrame
df = pd.DataFrame(data)
df.columns = df.iloc[0]  # Define a primeira linha como cabeçalho
df = df[1:].reset_index(drop=True)  # Remove a primeira linha antiga e reseta o índice

# Dicionário de substituição (ajuste conforme legenda do PDF)
df = df.rename(columns={'OD': 'Seg. Odontológica'})
df = df.rename(columns={'AMB': 'Seg. Ambulatorial'})

# Salva em CSV
csv_file = "Rol_de_Procedimentos.csv"
df.to_csv(csv_file, index=False, encoding="utf-8")

print(f"Arquivo {csv_file} salvo com sucesso!")

# Nome do ZIP final
zip_name = "Teste_Murilo.zip"

# Compacta o CSV
with zipfile.ZipFile(zip_name, "w") as zipf:
    zipf.write(csv_file)
    print(f"{csv_file} adicionado ao {zip_name}")

print(f"Arquivo {zip_name} criado com sucesso!")