import csv
import random
from datetime import datetime, timedelta

# Lista dos produtos com preços iniciais
produtos = [
    ("Samsung Galaxy A15 4G Dual SIM 128 GB Azul escuro 4 GB RAM", 848.9),
    ("Tênis Grand Court Cloudfoam Comfort adidas", 189.99),
    ("Monitor Gamer Samsung T350 24” FHD, Tela Plana, 75Hz, 5ms, HDMI, FreeSync, Game Mode", 589.0),
    ("Notebook Acer Asp3 A315-510p-34xc I3 8gb 256gb Ssd 15.6 W11", 2276.0),
    ("Mondial  Cozinha 4675-02 AFN-40-BFT Preto 110V", 298.9),
    ("Samsung Galaxy A15 4G Dual SIM 128 GB Azul claro 4 GB RAM", 858.9),
    ("Impressora Multifuncional 3 Em 1 Ecotank L3250 Preta Epson Cor Preto Bivolt", 993.13),
    ("Philco  PMO23EB Branco 220V", 499.0),
    ("Notebook Samsung Galaxy Book2 I5-1235u Windows 11 Home 8gb 256gb Ssd Grafite", 2829.0),
    ("Notebook Acer A315-24p-r611 R5 8gb 256gb Ssd 15.6'' W11h Cor Prateado", 2479.0),
    ("Fritadeira Air Fryer Oven Philco Pfr2200 4 Em 1 12l 1800w Cor Preta 110V", 697.46),
    ("Kit Com 5 Camisetas Masculinas Básicas Hering", 144.49),
    ("Creatina Monohidratada 500g Soldiers Nutrition Sabor Natural", 100.7),
    ("Kit 5 Camisetas Básicas Masculina Dry Fit Lisa Tradicional", 59.9),
    ("Motorola Moto G54 5G 256 GB Azul 8 GB RAM", 1127.0),
    ("Smart Tv 50pug7408/78 50 4k Google Tv Uhd Led Philips", 1999.0),
    ("Impressora a cor multifuncional Epson EcoTank L3250 com wifi preta 110V", 993.13),
    ("Mercado Pago: Point Pro2 - A Maquininha De Cartão + Completa", 118.72),
    ("Tênis Under Armour Essential 2 Original Academia Masculino", 189.99),
    ("Smart Tv 43'' Android Dolby Aws-tv-43-bl-02-a Aiwa Bivolt", 1439.0),
    ("Micro-ondas Electrolux de bancada Branco com Função Tira Odor e Manter Aquecido 34L MEO44 127v", 697.0),
    ("Darrow Actine gel de limpieza facial com vitamina C 400gr", 56.9),
    ("Creatina Monohidratada 600g 100% Pura Soldiers Nutrition", 112.42),
    ("Kit Com 10 Cuecas Boxer Algodão Sem Costura Zorba", 158.9),
    ("Smartphone Motorola Moto g04s 128GB 8GB Ram Boost Camera 16MP com Moto AI sensor FPS lateral - Grafite", 698.4),
    ("Smart TV LG 32’’ LED HD 32LQ621 Bivolt Preta - Experiência Visual Incrível", 1089.0),
    ("Kit Com 5 Camisetas Masculinas Básicas Hering", 134.99),
    ("Lavadora De Alta Pressão 1500w 1750psi Wap Ousada Plus 2200 110V", 489.0),
    ("Sofá Retrátil/reclinável Verona 2,00m Velut Cinza C/ Molas", 1025.0),
    ("Taiff Black Ion Secador De Cabelo Profissional Original2000w Cor Preto 110V", 231.04),
    ("Samsung Galaxy A15 Dual SIM 4G 256GB Azul claro 8GB RAM", 1033.0),
    ("Smart Tv 32'' Ptv32g7pr2csblh Roku Led Philco Bivolt", 999.9),
    ("Impressora a cor multifuncional Epson EcoTank L3250 com wifi preta 220V", 989.0),
    ("Parafusadeira Furadeira Sem Fio Bateria 12v P/ Madeira Metal Cor Amarelo/Preto Frequência 60 110V/220V", 159.9),
    ("Notebook Acer Aspire 5 A515-57-55b8 Intel Core I5 8gb 256gb SSD 15,6'' W11", 2718.0),
    ("Máquina de lavar automática Colormaq LCA - 12kg branca 127 V", 1459.0),
    ("Motorola Moto G84 5G 256GB Grafite 8GB RAM", 1335.0),
    ("Smart Tv Led 32 Hd Samsung Ls32betblggxzd 2 Hdmi 1 Usb Wifi", 1129.0),
    ("Cozinha Compacta Suspensa 7 Pts 2 Gavetas Juliete Nicioli Cor Carvalho Nature/Chumbo", 399.49),
    ("Micro-ondas NN-ST66NBRU 34L Black Glass Potência de 900W Cor Preto Panasonic 110V", 699.0),
    ("Kit 2 Câmera Ip Wifi Dome Rotativa Visão Noturna A8 Cor Branco", 196.65),
    ("Console padrão Ps5 Slim Bundle Ratchet & Clank and Returnal Cor Branco", 3849.0),
    ("Motorola Moto G24 128GB Rosa 8GB RAM", 729.0),
    ("Smart TV LG AI ThinQ 43LM631C0SB LED webOS Full HD 43'' 100V/240V", 1599.0),
    ("Micro-ondas Efficient 23 Litros Me23b Branco Electrolux 110v", 587.78),
    ("Loção hidratante Cerave Com Ácido Hialurônico Sem Perfume 473ml", 78.76),
    ("Notebook Lenovo Ideapad Celeron 4gb 128ssd 15.6 W11 C/office Cor Cinza", 1799.0),
    ("Samsung Galaxy A15 128gb Azul-escuro 4gb RAM Tela 6.5 90hz 5G Dual SIM", 929.0),
    ("Fritadeira Air Fryer New Pratic Af-31 Preto Mondial 127v", 284.0),
    ("Modulo Taramps Ts400x4 400w 2 Ohms Rca Ts 400x4 4 Canais 100w Amplificador 400rms T400 4 Canais Potencia Taramps Som Para Carro Moto Caminhonete Automotivo", 187.9),
    ("Smart TV 50'' Crystal UHD 4K 50CU8000 Design Air Slim 2023 Cor Cinza Titan Samsung 110V/220V", 2386.0)
]

# Data atual
data_atual = datetime.now()

# Função para gerar preços variados
def gerar_precos_variados(preco_base):
    return [round(preco_base + random.uniform(-0.1, 0.1) * preco_base, 2) for _ in range(7)]

# Geração dos dados
dados_variados = []
for produto, preco in produtos:
    precos_variados = gerar_precos_variados(preco)
    for i in range(7):
        data_variada = (data_atual - timedelta(days=i)).strftime('%Y-%m-%d')
        dados_variados.append([produto, precos_variados[i], data_variada])

# Nome do arquivo
nome_arquivo = 'product_prices.csv'

# Escrita do arquivo CSV
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["title", "price", "date"])
    writer.writerows(dados_variados)
