# Generated by Django 3.2.4 on 2021-06-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('phone_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=100)),
            ],
        ),
    ]