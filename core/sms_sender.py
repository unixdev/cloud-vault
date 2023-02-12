import requests
from cloud_vault.settings import SMS_API_KEY

from logging import getLogger

logger = getLogger('vault.core')


def send(phone, message):
    """
    Send an SMS to the given phone number.

    Parameters:
        phone: The phone number, e.g. 01712345678
        message: The text message to send
    """
    logger.debug('sending sms to phone %s', phone)

    payload = {
        'api_key': SMS_API_KEY,
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
