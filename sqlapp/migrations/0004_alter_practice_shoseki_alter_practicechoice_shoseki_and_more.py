# Generated by Django 4.2.7 on 2024-01-02 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0003_alter_practicechoice_thumbnaila1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='shoseki',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sqlapp.book', verbose_name='書籍・HP'),
        ),
        migrations.AlterField(
            model_name='practicechoice',
            name='shoseki',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sqlapp.book', verbose_name='書籍・HP'),
        ),
        migrations.CreateModel(
            name='Codepractice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.TextField(verbose_name='問題')),
                ('question2', models.TextField(verbose_name='問題')),
                ('question3', models.TextField(verbose_name='問題')),
                ('req1', models.TextField(blank=True, null=True, verbose_name='要件')),
                ('req2', models.TextField(blank=True, null=True, verbose_name='要件')),
                ('req3', models.TextField(blank=True, null=True, verbose_name='要件')),
                ('answer1', models.TextField(verbose_name='正解1')),
                ('answer2', models.TextField(blank=True, null=True, verbose_name='正解2')),
                ('answer3', models.TextField(blank=True, null=True, verbose_name='正解3')),
                ('answer4', models.TextField(blank=True, null=True, verbose_name='正解4')),
                ('answer5', models.TextField(blank=True, null=True, verbose_name='正解5')),
                ('thumbnailQ1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像1 (問題用)')),
                ('thumbnailQ2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像2 (問題用)')),
                ('thumbnailQ3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像3 (問題用)')),
                ('thumbnailQ4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像4 (問題用)')),
                ('thumbnailQ5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5 (問題用)')),
                ('explanation', models.TextField(blank=True, null=True, verbose_name='解説')),
                ('thumbnailA1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像1 (正解用)')),
                ('thumbnailA2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像2 (正解用)')),
                ('thumbnailA3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像3 (正解用)')),
                ('thumbnailA4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像4 (正解用)')),
                ('thumbnailA5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5 (正解用)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shoseki_page', models.CharField(blank=True, max_length=255, null=True, verbose_name='書籍ページ・HP何問目')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sqlapp.category', verbose_name='カテゴリ')),
                ('shoseki', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sqlapp.book', verbose_name='書籍・HP')),
            ],
        ),
    ]
