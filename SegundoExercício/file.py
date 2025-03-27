import pdfplumber
import pandas as pd

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

# Exibe as primeiras linhas
print(df.head())