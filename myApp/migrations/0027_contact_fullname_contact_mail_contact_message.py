# Generated by Django 5.0.2 on 2024-04-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0026_remove_savedaddress_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='fullname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mail',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
