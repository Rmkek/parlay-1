# Generated by Django 2.0.1 on 2018-02-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='books_read',
            field=models.ManyToManyField(to='index.Book'),
        ),
    ]
