# Generated by Django 2.2.5 on 2020-03-11 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('BMW', 'БМВ'), ('AUDI', 'Ауди'), ('TESLA', 'Тесла')], default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='test',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
