import requests
from bs4 import BeautifulSoup

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
    
    