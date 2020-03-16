# Generated by Django 2.1.1 on 2020-03-17 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_section', models.BooleanField(verbose_name='Основной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
            options={
                'verbose_name': 'Раздел статьи',
                'verbose_name_plural': 'Разделы статьи',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sections', models.CharField(max_length=256, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.AddField(
            model_name='articlesection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Section'),
        ),
        migrations.AddField(
            model_name='article',
            name='sections',
            field=models.ManyToManyField(through='articles.ArticleSection', to='articles.Section'),
        ),
    ]
