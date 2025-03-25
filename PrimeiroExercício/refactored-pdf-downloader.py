import os
import requests
from bs4 import BeautifulSoup
import zipfile
import logging
from typing import List

# Configuração de logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PDFDownloader:
    """
    Classe responsável por baixar PDFs de uma página web e compactá-los.
    """
    def __init__(self, url: str):
        """
        Inicializa o downloader com a URL da página.
        
        :param url: URL da página web para extrair links de PDF
        """
        self.url = url
        self.pdf_links = []
        self.file_names = ["Anexo_I.pdf", "Anexo_II.pdf"]

    def fetch_pdf_links(self) -> List[str]:
        """
        Busca links de PDFs na página web.
        
        :return: Lista de links de PDFs
        :raises requests.RequestException: Erro na requisição web
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Lança exceção para códigos de erro HTTP

            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a", href=True)
            
            self.pdf_links = [
                link["href"] for link in links 
                if link["href"].endswith(".pdf") and 
                any(anexo in link["href"] for anexo in ["Anexo_I", "Anexo_II"])
            ]
            
            logger.info(f"Encontrados {len(self.pdf_links)} links de PDF")
            return self.pdf_links
        
        except requests.RequestException as e:
            logger.error(f"Erro ao acessar a página: {e}")
            raise

    def download_pdfs(self) -> bool:
        """
        Baixa os PDFs encontrados.
        
        :return: True se todos os PDFs forem baixados com sucesso, False caso contrário
        """
        if not self.pdf_links:
            logger.warning("Nenhum link de PDF encontrado")
            return False

        try:
            for link, name in zip(self.pdf_links, self.file_names):
                response = requests.get(link, stream=True)
                response.raise_for_status()

                with open(name, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):  
                        file.write(chunk)
                
                logger.info(f"{name} baixado com sucesso!")
            
            return True
        
        except requests.RequestException as e:
            logger.error(f"Erro ao baixar PDFs: {e}")
            return False

    def create_zip_archive(self, zip_name: str = "anexos.zip") -> bool:
        """
        Cria um arquivo ZIP com os PDFs baixados.
        
        :param zip_name: Nome do arquivo ZIP
        :return: True se o ZIP for criado com sucesso, False caso contrário
        """
        try:
            with zipfile.ZipFile(zip_name, "w") as zipf:
                for pdf in self.file_names:
                    if os.path.exists(pdf):
                        zipf.write(pdf)
                        logger.info(f"{pdf} adicionado ao {zip_name}")
            
            logger.info(f"Arquivo {zip_name} criado com sucesso!")
            return True
        
        except Exception as e:
            logger.error(f"Erro ao criar arquivo ZIP: {e}")
            return False

    def cleanup(self):
        """
        Remove os arquivos PDF individuais após criação do ZIP.
        """
        try:
            for pdf in self.file_names:
                if os.path.exists(pdf):
                    os.remove(pdf)
                    logger.info(f"Arquivo {pdf} removido")
        except Exception as e:
            logger.error(f"Erro na limpeza dos arquivos: {e}")

def main():
    """
    Função principal para execução do script.
    """
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    try:
        downloader = PDFDownloader(url)
        
        # Busca links de PDFs
        downloader.fetch_pdf_links()
        
        # Baixa PDFs
        if downloader.download_pdfs():
            # Cria arquivo ZIP
            if downloader.create_zip_archive():
                # Remove arquivos individuais
                downloader.cleanup()
    
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
