# Generated by Django 4.1 on 2022-08-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0009_remove_item_contents'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='contents',
            field=models.TextField(default=' '),
        ),
    ]
