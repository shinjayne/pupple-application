# Generated by Django 3.1.1 on 2020-09-19 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_auto_20200912_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppablecontents',
            name='share',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
