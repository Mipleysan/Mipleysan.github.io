import requests
from bs4 import BeautifulSoup
from tabula import read_pdf
import pandas as pd
import numpy as np

url = 'https://www.petroperu.com.pe/productos/lista-de-precios-en-nuestras-plantas/'
urlB = 'https://www.petroperu.com.pe'
file = requests.get(url, verify='path/petroperu-com-pe-chain.pem')
soup = BeautifulSoup(file.text, "html.parser")
result =soup.find('a', attrs={'class': 'icon application-pdf'})
data = result.get('href')
tabla = read_pdf(urlB + data, pages="all")
df = pd.DataFrame(tabla[4])

print(df)

