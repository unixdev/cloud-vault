# Generated by Django 4.1.6 on 2023-02-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_phone_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='note',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]