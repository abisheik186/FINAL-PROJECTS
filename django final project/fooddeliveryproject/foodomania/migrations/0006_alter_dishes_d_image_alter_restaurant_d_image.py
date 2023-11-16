# Generated by Django 4.2.4 on 2023-10-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodomania', '0005_alter_dishes_d_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes_d',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dish_uploads/'),
        ),
        migrations.AlterField(
            model_name='restaurant_d',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurants/'),
        ),
    ]
