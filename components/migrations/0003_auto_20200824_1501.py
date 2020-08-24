# Generated by Django 3.1 on 2020-08-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_auto_20200817_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='votecomponent',
            name='allow_multi_choices',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='votecomponent',
            name='img_aspect_ratio',
            field=models.FloatField(default=1.0),
        ),
    ]
