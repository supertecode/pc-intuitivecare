import requests
from bs4 import BeautifulSoup
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response  = requests.get(url)

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)
    pdf_links = [
    link["href"] for link in links 
    if link["href"].endswith(".pdf") and ("Anexo_I" in link["href"] or "Anexo_II" in link["href"])
] 
    for i, link in enumerate(pdf_links):
        print(f"PDF {i + 1}: {link}")
        
else: 
    print("Erro ao acessar a página:", response.status_code)
    

file_names = ["Anexo_I.pdf", "Anexo_II.pdf"]

for link, name in zip(pdf_links, file_names):
    response = requests.get(link, stream=True)
    if response.status_code == 200:
        with open(name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):  
                file.write(chunk)
        print(f"{name} baixado com sucesso!")
        
    else: 
        print(f"Erro ao baixar {name}: {response.status_code}")
        
zip_name = "anexos.zip"

# Criando o arquivo ZIP
with zipfile.ZipFile(zip_name, "w") as zipf:
    for pdf in file_names:
        zipf.write(pdf)  # Adiciona cada PDF ao ZIP
        print(f"{pdf} adicionado ao {zip_name}")

print(f"Arquivo {zip_name} criado com sucesso!")