# Generated by Django 3.1.1 on 2020-09-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemachine',
            name='coffee_machine_models',
            field=models.CharField(default='', max_length=50),
        ),
    ]
