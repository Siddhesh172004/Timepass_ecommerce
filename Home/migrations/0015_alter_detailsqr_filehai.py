# Generated by Django 4.0.2 on 2022-04-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_alter_detailsqr_filehai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsqr',
            name='Filehai',
            field=models.ImageField(default='', upload_to='Home\\qrsuccess\\images'),
        ),
    ]
