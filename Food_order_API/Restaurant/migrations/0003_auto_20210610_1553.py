# Generated by Django 3.2.4 on 2021-06-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_auto_20210610_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='restaurant_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]