# Generated by Django 2.0.4 on 2018-05-14 19:57

import django.core.validators
from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news_text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='news',
            name='pic',
            field=models.ImageField(default='home/static/home/images/casd.png', upload_to=home.models.get_image_path),
        ),
        migrations.AddField(
            model_name='news',
            name='sub_title',
            field=models.TextField(default='Sub-titulo', validators=[django.core.validators.MaxLengthValidator(50)]),
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.TextField(default='Title', validators=[django.core.validators.MaxLengthValidator(30)]),
        ),
    ]