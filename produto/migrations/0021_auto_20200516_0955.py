# Generated by Django 3.0.6 on 2020-05-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0020_auto_20200516_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='produto/'),
        ),
    ]
