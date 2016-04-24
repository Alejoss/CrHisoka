# -*- coding: utf-8 -*-

import tweepy
from datetime import datetime
import time
import random
import sqlite3
import os
from os.path import join

# Inputs
intervalo_raw = raw_input("Numero intervalo-minutos: ")

# Config API Twitter
access_token_twitter = "1884663464-cKUFhmqTVbEvxbkdOD0rBo1UyXwX20ZrbtseIQc"
access_token_twitter_secret = "cRHTzKI4vyRJNOqLUrfGf3ELiP9PFD8pZttRFNUgUm4h5"
consumer_key = "XwIbq6Zwl5rUYzIMheFwx9MXO"
consumer_secret = "5M8hBfTyklmTMZkCRJH9PPadQGmEaMOu3ptiBbTn8Gm7gal8ju"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_twitter, access_token_twitter_secret)
api = tweepy.API(auth)

# Dir Imágenes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_img = join(BASE_DIR, "ol_imagenes")

tweetear = True  # False evita q se envien tweets
conn = sqlite3.connect('Auto_tweets.db')
c = conn.cursor()


def randomizar_intervalo(intervalo_raw):
	random_int = random.choice([0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.5])
	intervalo = int(intervalo_raw)*60*random_int  # convertir a minutos
	return intervalo


def obtener_fila_tweet(filas):
	tweet_object = []
	puntaje = None
	for fila in filas:
		if fila[2] is not None:
			date_object = datetime.strptime(fila[2], "%Y-%m-%d %X.%f")
			# procesar fecha, encontrar timedeltas multiplicar por prioridades.
			ahora = datetime.today()
			tiempo_pasado = ahora - date_object
			nuevo_puntaje = tiempo_pasado*int(fila[1])
			if puntaje is None:
				puntaje = nuevo_puntaje
				tweet_object = fila
			else:
				if puntaje < nuevo_puntaje:
					puntaje = nuevo_puntaje
					tweet_object = fila
		else:
			tweet_object = fila
			break
	return tweet_object


def redactar_tweet(tweet_object, tipo, tipo_tweet):
	if tipo == "video":
		tema = tweet_object[3]
		titulo = tweet_object[0]
		bitly = tweet_object[4]
		if tipo_tweet == "contenido1":
			return "Archivamos el video '%s' (%s) en el tema #%s. #LET" % (titulo, bitly, tema)
		elif tipo_tweet == "contenido2":
			return "'%s' (%s), video del tema #%s. #LET" % (titulo, bitly, tema)
		else:
			return "Mira el video del tema #%s: '%s' (%s). #LET" % (tema, titulo, bitly)
	elif tipo == "post":
		tema = tweet_object[3]
		titulo = tweet_object[0]
		bitly = tweet_object[4]
		if tipo_tweet == "contenido1":
			return "Archivamos el post '%s' (%s) en el tema #%s. #LET" % (titulo, bitly, tema)
		elif tipo_tweet == "contenido2":
			return "'%s' (%s), el post del tema #%s. #LET" % (titulo, bitly, tema)
		else:
			return "Lee el post del tema #%s: '%s' (%s), recomendado. #LET" % (tema, titulo, bitly)
	elif tipo == "frase":
		bitly = tweet_object[4]
		autor_completo = tweet_object[3]
		apellido_autor = autor_completo.rsplit(" ", 1)[-1]
		frase_completa = tweet_object[0]
		autor_frase = "%s: '%s'" % (apellido_autor, frase_completa)
		if len(autor_frase) > 115:
			slice_frase = autor_frase[:115]
			frase_final = "%s...%s" % (slice_frase, bitly)
		else:
			frase_final = "%s (%s)" % (autor_frase, bitly)

		return frase_final


def enviar_tweet(tweet, imagen):
	if imagen is None:
		try:
			tweet_enviado = api.update_status(tweet)
			print "Tweet: %s" % (tweet_enviado.text)
			print "caracteres: %s" % (len(tweet_enviado.text))
		except tweepy.TweepError as error:
			print "ERROR!:"
			print error
			print "caracteres: %s" % (len(tweet))
	else:
		try:
			tweet_enviado = api.update_with_media(str(imagen), tweet)
			print "Tweet: %s" % (tweet_enviado.text)
			print "caracteres: %s" % (len(tweet_enviado.text))
		except tweepy.TweepError as error:
			print "ERROR!:"
			print error
			print "caracteres: %s" % (len(tweet))


# Tweets temas
dict_temas = {}
with open("temas_bitlys.txt") as temas:
		content = temas.readlines()
		for line in content:
			tema, bitly = line.split(',')
			dict_temas[tema] = bitly

# counter para tener una cuenta de cuantos tweets van
counter = 0

lista_tipo_tweets_base = ["propio", "imagen", "frase", "imagen", "contenido2", "imagen",
							"contenido3", "imagen", "contenido1", "imagen", "contenido3",
							"imagen", "frase", "imagen", "contenido2", "imagen",
							"propio", "imagen", "contenido1", "imagen", "frase"]


lista_tipo_tweets = list(lista_tipo_tweets_base)

while True:
	ahora = datetime.today()
	ahora_str = str(ahora)
	if ahora.hour > 6:
		# No twitear antes de las 6am

		if len(lista_tipo_tweets) <= 3:
			lista_tipo_tweets = list(lista_tipo_tweets_base)

		for r in range(2):
			tipo_tweet = lista_tipo_tweets.pop(random.randint(0, (len(lista_tipo_tweets))-1))
			print str(counter) + " " + tipo_tweet + " --> " + ahora.strftime("%X")
			if tipo_tweet == "frase":
				filas = c.execute('SELECT * FROM TWEETS_FRASES ORDER BY ULTIMO_TWEET LIMIT 3')
				fila_tweet = obtener_fila_tweet(filas)
				tweet = redactar_tweet(fila_tweet, "frase", tipo_tweet)

				if tweetear:
					enviar_tweet(tweet, None)
					c.execute("UPDATE TWEETS_FRASES SET ULTIMO_TWEET = ? WHERE bitly = ?", (ahora_str, fila_tweet[4]))
					conn.commit()

			elif tipo_tweet == "contenido1" or tipo_tweet == "contenido2" or tipo_tweet == "contenido3":
				filas = c.execute('SELECT * FROM TWEETS ORDER BY ULTIMO_TWEET LIMIT 3')
				fila_tweet = obtener_fila_tweet(filas)
				tweet = redactar_tweet(fila_tweet, fila_tweet[5], tipo_tweet)

				if tweetear:
					enviar_tweet(tweet, None)
					c.execute("UPDATE TWEETS SET ULTIMO_TWEET = ? WHERE TITULO = ?", (ahora_str, fila_tweet[0]))
					conn.commit()

			elif tipo_tweet == "imagen":
				filas = c.execute('SELECT * FROM TWEETS_IMG ORDER BY ULTIMO_TWEET LIMIT 3')
				fila_tweet = obtener_fila_tweet(filas)
				texto_tweet = fila_tweet[3]
				tweet = "%s - http://bit.ly/olib_galeria" % (texto_tweet)
				ruta_temp = fila_tweet[0]

				print "ruta_temp: %s" % ruta_temp

				if tweetear:
					enviar_tweet(tweet, ruta_temp)
					c.execute("UPDATE TWEETS_IMG SET ULTIMO_TWEET = ? WHERE PATH_IMG = ?",
						     (ahora_str, ruta_temp))
					conn.commit()

			elif tipo_tweet == "propio":
				filas = c.execute('SELECT * FROM TWEETS_PROPIOS ORDER BY ULTIMO_TWEET LIMIT 3')
				fila_tweet = obtener_fila_tweet(filas)
				tweet = fila_tweet[0]

				if tweetear:
					enviar_tweet(tweet, None)
					c.execute("UPDATE TWEETS_PROPIOS SET ULTIMO_TWEET = ? WHERE TEXTO = ?",
						     (ahora_str, fila_tweet[0]))
					conn.commit()

			counter += 1
			time.sleep(300)

	print "-------------"

	tiempo_espera = randomizar_intervalo(intervalo_raw)
	time.sleep(float(tiempo_espera))
