# Generated by Django 3.0.6 on 2020-05-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_auto_20200516_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
