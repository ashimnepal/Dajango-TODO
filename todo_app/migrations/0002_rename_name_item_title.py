# Generated by Django 4.1 on 2022-08-13 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='title',
        ),
    ]
