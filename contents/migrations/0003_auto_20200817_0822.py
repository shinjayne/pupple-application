# Generated by Django 3.1 on 2020-08-17 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20200813_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubecontents',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='look',
            name='youtube_contents',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='look_set', to='contents.youtubecontents'),
        ),
        migrations.AlterField(
            model_name='youtubecontents',
            name='shoppable_contents',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='youtube_contents_set', to='contents.shoppablecontents'),
        ),
    ]