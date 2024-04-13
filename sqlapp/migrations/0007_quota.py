# Generated by Django 4.2.7 on 2024-01-07 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0006_alter_codepractice_question2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_count', models.IntegerField(default=0)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sqlapp.category')),
            ],
        ),
    ]
