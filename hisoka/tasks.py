from __future__ import absolute_import

from celery.decorators import task

@task
def prueba_celery(x, y):
    print x + y
    return x + y
