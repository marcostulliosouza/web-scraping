from product_scraper import ProductScraper

if __name__ == "__main__":
    URL = 'https://www.mercadolivre.com.br/ofertas#nav-header'
    HEADERS = {'User-Agent': 'Mozilla/5.0'}

    scraper = ProductScraper(URL, HEADERS)
    scraper.automate_collection(interval=86400)  # Coleta dados a cada 24 horas


