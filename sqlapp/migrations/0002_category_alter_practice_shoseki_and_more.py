# Generated by Django 4.2.7 on 2023-12-30 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='practice',
            name='shoseki',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqlapp.book', verbose_name='書籍・HP'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='shoseki_page',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='書籍ページ・HP何問目'),
        ),
        migrations.CreateModel(
            name='PracticeChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='問題')),
                ('thumbnailQ1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像1 (問題)')),
                ('thumbnailQ2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像2 (問題)')),
                ('thumbnailQ3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像3 (問題)')),
                ('answer', models.TextField(verbose_name='正解')),
                ('wronganswer1', models.TextField(blank=True, null=True, verbose_name='誤回答1')),
                ('wronganswer2', models.TextField(blank=True, null=True, verbose_name='誤回答2')),
                ('wronganswer3', models.TextField(blank=True, null=True, verbose_name='誤回答3')),
                ('wronganswer4', models.TextField(blank=True, null=True, verbose_name='誤回答4')),
                ('wronganswer5', models.TextField(blank=True, null=True, verbose_name='誤回答5')),
                ('wronganswer6', models.TextField(blank=True, null=True, verbose_name='誤回答6')),
                ('wronganswer7', models.TextField(blank=True, null=True, verbose_name='誤回答7')),
                ('wronganswer8', models.TextField(blank=True, null=True, verbose_name='誤回答8')),
                ('wronganswer9', models.TextField(blank=True, null=True, verbose_name='誤回答9')),
                ('explanation', models.TextField(blank=True, null=True, verbose_name='解説')),
                ('thumbnailA1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像1 (正解)')),
                ('thumbnailA2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像2 (正解)')),
                ('thumbnailA3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像3 (正解)')),
                ('hint1', models.TextField(blank=True, null=True, verbose_name='ヒント1')),
                ('hint2', models.TextField(blank=True, null=True, verbose_name='ヒント2')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shoseki_page', models.CharField(blank=True, max_length=255, null=True, verbose_name='書籍ページ')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sqlapp.category', verbose_name='カテゴリ')),
                ('shoseki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqlapp.book', verbose_name='書籍・HP')),
            ],
        ),
        migrations.AddField(
            model_name='practice',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sqlapp.category', verbose_name='カテゴリ'),
        ),
    ]
