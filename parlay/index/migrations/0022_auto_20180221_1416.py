# Generated by Django 2.0.2 on 2018-02-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_auto_20180220_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='Description for the book'),
        ),
    ]