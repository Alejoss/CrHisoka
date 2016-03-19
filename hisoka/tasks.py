from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
from hisoka.models import FeralSpirit, Fireball


@task()
def create_fireball(request):
    fireball = Fireball.objects.last()
    FeralSpirit.objects.create(fireball=fireball, tipo="prueba", nombre="prueba")

    logger.info("En teoria algo paso")


"""
logger = get_task_logger(__name__)
@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="task_periodica_de_prueba",
    ignore_result=True
)
def task_craate_fireball():
    fireball = Fireball.objects.last()
    FeralSpirit.objects.create(fireball=fireball, tipo="prueba", nombre="prueba")

    logger.info("En teoria algo paso")
"""
