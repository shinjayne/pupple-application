# Generated by Django 3.1.1 on 2020-09-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200912_1334'),
        ('components', '0009_auto_20200912_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_comment_set', to='accounts.IPUserProfile'),
        ),
    ]
