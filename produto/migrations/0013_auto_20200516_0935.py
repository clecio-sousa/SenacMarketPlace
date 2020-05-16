# Generated by Django 3.0.6 on 2020-05-16 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0012_auto_20200516_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='image',
        ),
        migrations.AddField(
            model_name='produto',
            name='url',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='url_imagem',
            field=models.URLField(blank=True, max_length=10000, null=True),
        ),
    ]
