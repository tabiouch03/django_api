# Generated by Django 3.0.8 on 2020-07-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_game', '0004_auto_20200703_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=10),
        ),
    ]
