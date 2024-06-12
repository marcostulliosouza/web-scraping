from product_scraper import ProductScraper

if __name__ == "__main__":
    scraper = ProductScraper(None, None)
    scraper.load_data('product_prices.csv')
    scraper.plot_price_variation()
