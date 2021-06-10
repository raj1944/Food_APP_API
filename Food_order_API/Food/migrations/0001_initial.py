# Generated by Django 3.2.4 on 2021-06-10 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='Branch.branch')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='Food.food')),
            ],
        ),
    ]