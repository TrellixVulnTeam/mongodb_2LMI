# Generated by Django 2.2.2 on 2019-07-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='signup',
            field=models.DateTimeField(),
        ),
    ]
