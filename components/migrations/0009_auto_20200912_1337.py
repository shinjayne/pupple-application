# Generated by Django 3.1 on 2020-09-12 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200912_1334'),
        ('components', '0008_auto_20200912_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='random_writer_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to='accounts.ipuserprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votechoice',
            name='voted_users',
            field=models.ManyToManyField(blank=True, to='accounts.IPUserProfile'),
        ),
    ]
