# Generated by Django 4.1 on 2022-08-13 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_name_item_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
    ]
