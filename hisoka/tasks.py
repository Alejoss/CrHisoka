# coding=utf-8
from datetime import datetime
import random
import os

import tweepy

from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
from hisoka.models import FeralSpirit, Fireball

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/10')),
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

    # api = twitter.Api(access_token_key=access_token_twitter,
    #                   access_token_secret=access_token_twitter_secret,
    #                   consumer_key=consumer_key,
    #                   consumer_secret=consumer_secret)

    # Obtener FeralSpirits
    # Toma los 3 feralspirits con fecha de publicación más lejana, luego elige uno random
    feral_spirits = FeralSpirit.objects.filter(activo=True, eliminado=False, fireball=fireball_orilla)[:3]
    lista_ferals = [f for f in feral_spirits]
    feral_elegido = random.choice(lista_ferals)

    texto_tweet = "%s %s" % (feral_elegido.texto, feral_elegido.url)

    # Enviar Tweet
    if feral_elegido.tipo == "imagen":
        # Envia tweets de Orilla Libertaria a twitter

        filename = feral_elegido.imagen.file.name
        media_ids = api.media_upload(filename=filename)

        params = {'status': texto_tweet, 'media_ids': [media_ids.media_id_string]}
        api.update_status(**params)

    else:
        api.update_status(texto_tweet)

    # Aumentar contador
    # logger(logger.info("tweet enviado id: %s" % feral_elegido.id))
    feral_elegido.aumentar_contador()

    # Actualizar fecha ultimo tweet
    feral_elegido.ultima_publicacion = datetime.today()
    feral_elegido.save()
