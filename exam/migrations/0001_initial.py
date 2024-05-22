# Generated by Django 5.0.6 on 2024-05-22 09:12

import django.db.models.deletion
import exam.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('image', models.ImageField(blank=True, null=True, upload_to=exam.models.Science.scienceImage)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='science',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.science'),
        ),
    ]
