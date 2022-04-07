# Generated by Django 4.0.2 on 2022-04-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_alter_detailsqr_filehai'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='CODHai',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='UPIHai',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='detailsqr',
            name='Filehai',
            field=models.ImageField(default='', upload_to='Home\\qrdetails\\images'),
        ),
    ]