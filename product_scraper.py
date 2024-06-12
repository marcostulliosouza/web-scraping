import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import matplotlib.pyplot as plt


class ProductScraper:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.data = pd.DataFrame(columns=['title', 'price', 'date'])

    def fetch_page(self):
        print("Fazendo requisição para:", self.url)
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            print("Requisição bem-sucedida!")
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print("Erro na requisição! Status code:", response.status_code)
            return None

    def extract_product_info(self, soup):
        products = []
        for item in soup.select('.promotion-item'):
            title = item.select_one('.promotion-item__title').text.strip()
            price_main_tag = item.select_one('.andes-money-amount-combo__main-container')
            price_fraction_tag = price_main_tag.select_one('.andes-money-amount__fraction')
            price_cents_tag = price_main_tag.select_one('.andes-money-amount__cents')
            if price_fraction_tag:
                price_text = price_fraction_tag.text.strip()
                price = float(price_text.replace('.', '').replace(',', '.'))
                if price_cents_tag:
                    price_cents_text = price_cents_tag.text.strip()
                    price += float(price_cents_text) / 100
                products.append({'title': title, 'price': price, 'date': datetime.now().date()})
                print("Dados extraídos para:", title)
            else:
                print("Não foi possível extrair dados para:", title)
        return products

    def collect_data(self):
        print("Iniciando coleta de dados...")
        soup = self.fetch_page()
        if soup:
            products = self.extract_product_info(soup)
            if products:
                new_data = pd.DataFrame(products)
                if self.data.empty:
                    self.data = new_data
                else:
                    self.data = pd.concat([self.data, new_data], ignore_index=True)
                print("Dados coletados com sucesso!")
            else:
                print("Nenhum dado foi extraído. Verifique os seletores CSS.")
        else:
            print("Falha ao obter a página. Verifique a URL e sua conexão com a internet.")

    def save_data(self, filename='product_prices.csv'):
        self.data.to_csv(filename, index=False)
        print("Dados salvos em:", filename)

    def load_data(self, filename='product_prices.csv'):
        self.data = pd.read_csv(filename)
        print("Dados carregados de:", filename)

    def automate_collection(self, interval=86400):
        print("Coleta automática iniciada. Pressione Ctrl+C para interromper.")
        while True:
            self.collect_data()
            self.save_data()
            time.sleep(interval)

    def plot_price_variation(self):
        if not self.data.empty:
            # Calculando a variação percentual em relação ao preço inicial
            initial_prices = self.data.groupby('title')['price'].first()
            self.data['price_variation'] = (self.data['price'] - self.data['title'].map(initial_prices)) / self.data[
                'title'].map(initial_prices) * 100

            # Imprimir os valores calculados para cada produto
            print("Variação de preços calculada:")
            for product, variation in self.data.groupby('title')['price_variation'].last().items():
                print(f"{product}: {variation:.2f}%")

            # Plotando a variação de preços
            plt.figure(figsize=(12, 6))
            for product in self.data['title'].unique():
                product_data = self.data[self.data['title'] == product]
                short_title = product[:20] + '...' if len(
                    product) > 20 else product  # Mostra apenas os primeiros 20 caracteres
                plt.plot(product_data['date'], product_data['price_variation'], label=short_title, marker='o')

            plt.xlabel('Data')
            plt.ylabel('Variação de Preço (%)')
            plt.title('Variação de Preços dos Produtos ao Longo do Tempo')
            plt.legend(fontsize='small', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout(pad=2)
            # Ajuste do espaço inferior (bottom)
            plt.subplots_adjust(bottom=0.2)
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("Não há dados para plotar. Carregue os dados primeiro.")