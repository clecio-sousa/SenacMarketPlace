# Generated by Django 3.0.6 on 2020-05-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0027_auto_20200516_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]