from flask import Flask
from tabula import read_pdf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.petroperu.com.pe/productos/lista-de-precios-en-nuestras-plantas/'
urlB = 'https://www.petroperu.com.pe'
file = requests.get(url, verify='path/petroperu-com-pe-chain.pem')
soup = BeautifulSoup(file.text, "html.parser")
result =soup.find('a', attrs={'class': 'icon application-pdf'})
data = result.get('href')
tabla = read_pdf(urlB + data, pages="all")
#df = pd.DataFrame(tabla[4])


app = Flask(__name__)

@app.route('/')

def home():
    return str(tabla[4])


if __name__ in ('__main__'):
    app.run()(debug=True)