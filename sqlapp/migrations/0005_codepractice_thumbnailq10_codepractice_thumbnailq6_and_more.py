# Generated by Django 4.2.7 on 2024-01-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0004_alter_practice_shoseki_alter_practicechoice_shoseki_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='codepractice',
            name='thumbnailQ10',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5 (問題用)'),
        ),
        migrations.AddField(
            model_name='codepractice',
            name='thumbnailQ6',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5 (問題用)'),
        ),
        migrations.AddField(
            model_name='codepractice',
            name='thumbnailQ7',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5 (問題用)'),
        ),
        migrations.AddField(
            model_name='codepractice',
            name='thumbnailQ8',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5 (問題用)'),
        ),
        migrations.AddField(
            model_name='codepractice',
            name='thumbnailQ9',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5 (問題用)'),
        ),
    ]