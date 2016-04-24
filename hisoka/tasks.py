# coding=utf-8
import requests
import tweepy
from datetime import datetime
import random
import os
from StringIO import StringIO
from PIL import Image

from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
from hisoka.models import FeralSpirit, Fireball

logger = get_task_logger(__name__)


def randomizar_intervalo(intervalo_raw):
    random_int = random.choice([0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.5])
    intervalo = int(intervalo_raw) * 60 * random_int  # convertir a minutos
    return intervalo


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="tweet_orilla",
    ignore_result=True
)
def tweet_orilla():
    fireball_orilla = Fireball.objects.get(nombre="OrillaLibertaria")
    # Envia tweets de Orilla Libertaria a twitter
    access_token_twitter = "1884663464-cKUFhmqTVbEvxbkdOD0rBo1UyXwX20ZrbtseIQc"
    access_token_twitter_secret = os.environ['ACCESS_TOKEN_TWITTER_SECRET']
    consumer_key = "XwIbq6Zwl5rUYzIMheFwx9MXO"
    consumer_secret = os.environ['CONSUMER_SECRET_TWITTER']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_twitter, access_token_twitter_secret)
    api = tweepy.API(auth)

    # Obtener FeralSpirits
    # Toma los 3 feralspirits con fecha de publicación más lejana, luego elige uno random
    feral_spirits = FeralSpirit.objects.filter(activo=True, eliminado=False, fireball=fireball_orilla)[:3]
    feral_elegido = feral_spirits.pop(random.randint(0, 2))

    # Redactar Tweet
    if feral_elegido.tipo == "video":
        texto = "%s (%s). video del tema %s #LET" % (feral_elegido.nombre, feral_elegido.url, feral_elegido.tema)
    elif feral_elegido.tipo == "post":
        texto = "%s (%s). post del tema %s #LET" % (feral_elegido.nombre, feral_elegido.url, feral_elegido.tema)
    elif feral_elegido.tipo == "frase":
        texto = "%s (%s)" % (feral_elegido.nombre, feral_elegido.url)
    elif feral_elegido.tipo == "imagen":
        texto = "Imagen (%s) en la Galería de Orilla Libertaria (%s) #LET" % (feral_elegido.url, feral_elegido.tema)
    else:
        texto = "feral sin tipo: %s" % feral_elegido.id

    # Loggear info sobre tweet a intentar
    logger.info(("feral id: %s" % feral_elegido.id) + " - " + texto)

    # Enviar Tweet
    try:
        if feral_elegido.tipo == "imagen":
            respuesta_imagen = requests.get(feral_elegido.url, stream=True)
            imagen = Image.open(StringIO(respuesta_imagen.content))
            api.update_with_media(imagen, texto)
        else:
            api.update_status(texto)

        # Aumentar contador
        logger(logger.info("tweet enviado id: %s" % feral_elegido.id))
        feral_elegido.aumentar_contador()

        # Actualizar fecha ultimo tweet
        feral_elegido.ultima_publicacion = datetime.today()
        feral_elegido.save()

    except tweepy.TweepError as error:
        logger.info("error: " + error)
