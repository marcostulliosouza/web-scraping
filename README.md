# Análise de Preços de Produtos de E-commerce

Este projeto coleta dados de preços de produtos de um site de e-commerce e analisa a variação de preços ao longo do tempo.

## Ferramentas Utilizadas
- Python
- BeautifulSoup
- Pandas
- Matplotlib
- Jupyter Notebook

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/marcostulliosouza/web-scraping.git
    cd web-scraping
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o script de coleta de dados:
    ```bash
    python collect_data.py
    ```

4. Execute o script de análise de dados:
    ```bash
    python collect_data.py
    ```
    
## Resultados
Os dados coletados são salvos em `product_prices.csv` e a análise de variação de preços é visualizada em gráfico.

### 5. **Estrutura de Arquivos**
- `product_scraper.py`: Contém a classe `ProductScraper`.
- `collect_data.py`: Script para iniciar a coleta automática de dados.
- `analyze_data.py`: Script para carregar e analisar os dados coletados.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Documentação do projeto.

### **Estrutura de Arquivos do Projeto**

```plaintext
price-analysis/
├── README.md
├── product_scraper.py
├── collect_data.py
├── analyze_data.py
└── requirements.txt

