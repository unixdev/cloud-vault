import requests
from django.conf import settings

from logging import getLogger

logger = getLogger('vault.core')


def send(phone, message):
    """
    Send an SMS to the given phone number.

    Parameters:
        phone: The phone number, e.g. 01712345678
        message: The text message to send
    """
    if settings.TESTING:
        logger.debug('skipping sending sms to phone %s', phone)
        return

    logger.debug('sending sms to phone %s', phone)

    payload = {
        'api_key': settings.SMS_API_KEY,
        'type': 'text',
        'contacts': '88' + phone,
        'senderid': 11209,
        'msg': message
    }
    r = requests.get('http://sms.viatech.com.bd/smsapi', params=payload)

    if r.status_code != 200:
        logger.error('error in sending SMS')
        r.raise_for_status()

    logger.debug('sent sms to phone %s', phone)
