# Generated by Django 3.1 on 2020-08-29 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_lookiteminfocomponent_look'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votecomponent',
            name='allow_multi_choices',
        ),
        migrations.AddField(
            model_name='votecomponent',
            name='allowed_choice_num',
            field=models.SmallIntegerField(default=1),
        ),
    ]