# Generated by Django 3.0.6 on 2020-05-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0024_auto_20200516_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
