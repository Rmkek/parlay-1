# Generated by Django 2.0.1 on 2018-03-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0025_book_cover_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='wager',
            name='until',
            field=models.DateField(null=True),
        ),
    ]
