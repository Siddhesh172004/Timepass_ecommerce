# Generated by Django 4.0.2 on 2022-04-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_detailsqr_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsqr',
            name='File',
            field=models.ImageField(default='https://via.placeholder.com/500x500.png?text=Default', upload_to='Home\\qrsuccess\\images'),
        ),
    ]
