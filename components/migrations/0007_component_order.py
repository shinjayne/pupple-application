# Generated by Django 3.1 on 2020-08-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0006_modelinfocomponent'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
