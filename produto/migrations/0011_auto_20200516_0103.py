# Generated by Django 3.0.6 on 2020-05-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0010_auto_20200516_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.URLField(blank=True, max_length=10000, null=True),
        ),
    ]
