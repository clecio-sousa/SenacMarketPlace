# Generated by Django 3.0.6 on 2020-05-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0011_auto_20200516_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.CharField(max_length=10000),
        ),
    ]
