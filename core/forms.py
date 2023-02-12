from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import User, Verification

from logging import getLogger

import secrets
import string

VERIFY_CODE_LENGTH = 6

logger = getLogger('vault.core')


def gen_verify_code():
    """Generate verification code."""
    code = ''.join(secrets.choice(string.digits) for i in range(VERIFY_CODE_LENGTH))
    return code


class SignupForm(UserCreationForm):
    """
    Create a user with phone and password.
    """
    class Meta:
        model = User
        fields = ('phone', 'email')

    def save(self, commit=True):
        if commit:
            code = gen_verify_code()
            with transaction.atomic():
                user = super().save(True)
                verification = Verification(user=user, code=code)
                verification.save()
            logger.info('set verification for %s with code: %s', user.phone, code)
            return user

        return super().save(False)


class VerificationForm(forms.Form):
    phone = forms.CharField(label=_('Phone Number'), max_length=11)
    code = forms.CharField(label=_('Verification Code'), max_length=6)

    def clean(self):
        super().clean()

        phone = self.cleaned_data['phone']
        code = self.cleaned_data['code']

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise ValidationError(_('Incorrect Phone Number'))

        if code != user.verification.code:
            raise ValidationError(_('Incorrect Verification Code'))

    def activate_user(self):
        user = User.objects.get(phone=self.cleaned_data['phone'])
        user.is_active = True
        with transaction.atomic():
            user.save()
            user.verification.delete()
        logger.info('activated user with phone %s', user.phone)
