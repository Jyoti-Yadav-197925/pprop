# Generated by Django 3.1.1 on 2022-01-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0013_auto_20220123_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='music_id',
            field=models.IntegerField(default=0),
        ),
    ]
