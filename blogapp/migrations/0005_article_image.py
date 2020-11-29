# Generated by Django 3.1.3 on 2020-11-29 06:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20201128_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blog_images'),
            preserve_default=False,
        ),
    ]
