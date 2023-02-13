from celery import shared_task
from .sms_sender import send

from logging import getLogger

logger = getLogger('vault.task')


@shared_task()
def send_task(phone, message):
    logger.info('executing send_task for phone %s', phone)
    send(phone, message)
