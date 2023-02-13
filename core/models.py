from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os import path

fs = FileSystemStorage(settings.STORAGE_DIR)


class User(AbstractBaseUser):
    """
    Custom user model.
    """
    phone = models.CharField(
        _('phone number'),
        validators=[RegexValidator(regex=r'^0[0-9]{10}$')],
        max_length=11,
        help_text='e.g. 01712345678',
        unique=True
    )
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


class Verification(models.Model):
    """
    Holds verification codes/OTP.
    """
    user = models.OneToOneField(User, models.CASCADE)
    code = models.CharField(_('verification code'), max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


def file_location(document, filename):
    return f'{document.user.id}/{filename}'


def validate_file_size(file):
    limit = 2 * 1024 * 1024
    if file.size > limit:
        raise ValidationError(_('Maximum allowed file size is 2MB'))


class Document(models.Model):
    """
    Represent and uploaded document/file.
    """
    user = models.ForeignKey(User, models.CASCADE)
    file = models.FileField(
        validators=[validate_file_size],
        upload_to=file_location,
        storage=fs,
    )
    note = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def basename(self):
        """return basename of the uploaded file"""
        return path.basename(self.file.name)
