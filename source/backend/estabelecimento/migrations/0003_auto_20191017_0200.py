# Generated by Django 2.2.5 on 2019-10-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0002_auto_20191015_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]