# Generated by Django 2.1.1 on 2020-03-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='students.Course'),
        ),
    ]
