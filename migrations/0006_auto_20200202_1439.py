# Generated by Django 3.0.2 on 2020-02-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_main_set_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='main',
            name='tell',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
