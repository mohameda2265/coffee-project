# Generated by Django 3.1.1 on 2020-09-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_auto_20200910_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeepod',
            name='coffee_flavor',
            field=models.CharField(max_length=50),
        ),
    ]