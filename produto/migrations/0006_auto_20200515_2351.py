# Generated by Django 3.0.6 on 2020-05-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20200515_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='templates/'),
        ),
    ]
