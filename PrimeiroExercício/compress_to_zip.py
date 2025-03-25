import zipfile

# Nome do arquivo ZIP final
zip_name = "anexos.zip"

# Lista com os arquivos PDF baixados
pdf_files = ["Anexo_I.pdf", "Anexo_II.pdf"]

# Criando o arquivo ZIP
with zipfile.ZipFile(zip_name, "w") as zipf:
    for pdf in pdf_files:
        zipf.write(pdf)  # Adiciona cada PDF ao ZIP
        print(f"{pdf} adicionado ao {zip_name}")

print(f"Arquivo {zip_name} criado com sucesso!")