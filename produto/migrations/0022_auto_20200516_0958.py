# Generated by Django 3.0.6 on 2020-05-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0021_auto_20200516_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
