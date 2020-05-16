# Generated by Django 3.0.6 on 2020-05-16 12:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0013_auto_20200516_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='url_imagem',
        ),
        migrations.AlterField(
            model_name='produto',
            name='url',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
    ]