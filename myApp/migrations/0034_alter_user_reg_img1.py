# Generated by Django 5.0.2 on 2024-04-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0033_alter_edit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='img1',
            field=models.ImageField(null=True, upload_to='profile-image/'),
        ),
    ]
