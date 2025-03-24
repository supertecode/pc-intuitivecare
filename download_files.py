import requests

links = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

file_names = ["Anexo_I.pdf", "Anexo_II.pdf"]

for link, name in zip(links, file_names):
    response = requests.get(link, stream=True)
    if response.status_code == 200:
        with open(name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):  
                file.write(chunk)
        print(f"{name} baixado com sucesso!")
        
    else: 
        print(f"Erro ao baixar {name}: {response.status_code}")
    