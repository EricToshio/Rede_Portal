# Generated by Django 2.0.5 on 2018-05-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('iniciativa_name', models.CharField(max_length=100)),
            ],
        ),
    ]
