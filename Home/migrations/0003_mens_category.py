# Generated by Django 4.0.2 on 2022-03-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_accessories_kids_womens_remove_mens_oldprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mens',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
