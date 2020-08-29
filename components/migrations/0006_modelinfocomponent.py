# Generated by Django 3.1 on 2020-08-29 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_auto_20200829_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelInfoComponent',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('height', models.CharField(blank=True, max_length=30)),
                ('top', models.CharField(blank=True, max_length=30)),
                ('bottom', models.CharField(blank=True, max_length=30)),
                ('shoes', models.CharField(blank=True, max_length=30)),
            ],
            bases=('components.component',),
        ),
    ]