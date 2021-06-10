# Generated by Django 3.2.4 on 2021-06-10 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Food', '0001_initial'),
        ('Branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField(default=0)),
                ('delivery_addr', models.CharField(blank=True, max_length=50)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Branch.branch')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='Food.menu')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='Order.order')),
            ],
        ),
    ]