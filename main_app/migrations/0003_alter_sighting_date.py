# Generated by Django 4.1.7 on 2023-03-05 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sighting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateField(verbose_name='sighting date'),
        ),
    ]
