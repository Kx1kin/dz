# Generated by Django 4.2.5 on 2023-09-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisments', '0002_alter_advertisement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='Advertisements',
        ),
    ]
