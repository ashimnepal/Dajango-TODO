# Generated by Django 4.1 on 2022-08-13 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0008_rename_content_item_contents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='contents',
        ),
    ]
