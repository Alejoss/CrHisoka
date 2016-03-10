
"""
script que saca imagenes de http://www.smfcorp.net dando un url, las corta y las guarda
"""
from bs4 import BeautifulSoup
import requests
from StringIO import StringIO
from PIL import Image


url = raw_input("url: ")

# Saca el codigo de la carta de la url bara buscar en el html
id_carta = url.split("/")
codigo_letra = ["carte"]
for letra in id_carta[3]:
    if letra.isdigit():
        codigo_letra.append(letra)

codigo_letra = "".join(codigo_letra)
print codigo_letra

# hace el request al url y guarda el html en una variable
r = requests.get(url)
html_pagina = r.text

# busca el div que tiene la imagen
soup = BeautifulSoup(html_pagina, 'html.parser')
div_imagen = soup.find_all("div", id=codigo_letra)

# saca la url de la imagen que esta dentro del background image en inline css
string_div = str(div_imagen[0])
letra_p_de_png = string_div.find("png")
letra_inicial = letra_p_de_png - 24
letra_final = letra_p_de_png + 3
path_a_imagen = string_div[letra_inicial:letra_final]
url_imagen = "http://www.smfcorp.net" + path_a_imagen
print url_imagen

# hacer otro request y guardar la imagen
r = requests.get(url_imagen, stream=True)
i = Image.open(StringIO(r.content))

imagen_cortada = i.crop((22, 44, 221, 165))
imagen_cortada.save("imagen_cortada.png")
