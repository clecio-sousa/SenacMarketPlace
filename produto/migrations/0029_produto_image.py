# Generated by Django 3.0.6 on 2020-05-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0028_produto_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
