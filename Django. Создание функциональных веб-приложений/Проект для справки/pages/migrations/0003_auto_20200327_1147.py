# Generated by Django 2.1.1 on 2020-03-27 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_title',
        ),
    ]
