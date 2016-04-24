"""
script que saca imagenes de http://www.smfcorp.net dando un url, las corta y las guarda
"""
from bs4 import BeautifulSoup
import requests
from StringIO import StringIO
from PIL import Image


from django.core.exceptions import ValidationError

def obtener_codigo_carta(url):
    """
    :param url: el url pegado que tiene la imagen.
    :return: un texto el codiga que corresponde a la carta
    """
    id_carta = url.split("/")
    codigo_letra = ["carte"]
    for letra in id_carta[3]:
        if letra.isdigit():
            codigo_letra.append(letra)

    codigo_letra = "".join(codigo_letra)
    return codigo_letra


def obtener_html(url, codigo_letra):
    """
    :param url: La url objetivo
    :param codigo_letra: el codigo que le corresponde a la carta
    :return: el div en string html que le contiene a la carta
    """
    r = requests.get(url)
    html_pagina = r.text

    # busca el div que tiene la imagen
    soup = BeautifulSoup(html_pagina, 'html.parser')
    div_imagen = soup.find_all("div", id=codigo_letra)

    return div_imagen


def obtener_url_imagen(div_imagen):
    """
    :param div_imagen: El div que tiene la imagen en el fondo en css
    :return: la url de la imagen
    """
    string_div = str(div_imagen[0])
    print "string_div: %s" % string_div

    # Busca las letras "png" o "jpg" dentro del div
    letra_j_de_jpg = -1
    letra_p_de_png = string_div.find("png")  # devuelve -1 si no encuentra
    if letra_p_de_png == -1:
        letra_j_de_jpg = string_div.find("jpg")
        if letra_j_de_jpg == -1:
            return False
        else:
            letra_utilizada = letra_j_de_jpg
    else:
        letra_utilizada = letra_j_de_jpg

    print "string_div: %s" % string_div
    letra_inicial = letra_utilizada - 24
    print "letra_inicial: %s" % letra_inicial
    letra_final = letra_utilizada + 3
    print "letra_final: %s" % letra_final
    path_a_imagen = string_div[letra_inicial:letra_final]
    print "path_a_imagen: %s" % path_a_imagen
    url_imagen = "http://www.smfcorp.net" + path_a_imagen

    return url_imagen


def obtener_imagen(url_imagen):
    """
    :param url_imagen: la url que contiene la imagen
    :return: La imagen recortada
    """
    # hacer otro request y guardar la imagen
    respuesta = requests.get(url_imagen, stream=True)
    imagen = Image.open(StringIO(respuesta.content))

    imagen_cortada = imagen.crop((22, 44, 221, 165))

    return imagen_cortada


def rakatica(url):
    """
    :param url: La url que contiene la imagen en la pagina
    :return: La imagen recortada lista para ser guardada
    """
    print "url %s: " % url
    codigo_carta = obtener_codigo_carta(url)

    print "codigo_carta: %s" % codigo_carta
    div_html = obtener_html(url, codigo_carta)

    print "div_html: %s" % div_html
    url_imagen = obtener_url_imagen(div_html)
    if not url_imagen:
        raise ValidationError("No se encontro la cadena con el texto del "
                              "archivo de la carta en el div")

    print "url_imagen: %s" % url_imagen
    imagen_recortada = obtener_imagen(url_imagen)

    return imagen_recortada
