# Generated by Django 2.0.5 on 2018-05-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='inciativa',
            new_name='iniciativa',
        ),
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(default='enviado', max_length=20),
        ),
    ]
