# Generated by Django 3.1.2 on 2020-11-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0002_auto_20201117_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='status_advert',
            field=models.BooleanField(default=True),
        ),
    ]