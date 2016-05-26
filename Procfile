web: gunicorn criptolibertad.wsgi --log-file -
worker: celery -A criptolibertad worker -events -loglevel info
beat: celery -A criptolibertad beat