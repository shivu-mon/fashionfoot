# Generated by Django 5.0.2 on 2024-03-11 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_alter_cart_cart_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user_reg')),
            ],
        ),
    ]
