# Generated by Django 5.0.6 on 2024-05-23 05:13

import assets.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('image', models.ImageField(blank=True, null=True, upload_to=assets.models.Science.scienceImage)),
            ],
            options={
                'verbose_name': 'Fan',
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=400)),
                ('abbr_name', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(max_length=300, upload_to='university_images/')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('keywords', models.CharField(blank=True, max_length=800)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'Universitet',
                'verbose_name_plural': 'Universitetlar',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.region')),
            ],
            options={
                'verbose_name': 'Tuman (Shahar)',
                'verbose_name_plural': 'Tuman (Shahar)lar',
            },
        ),
        migrations.CreateModel(
            name='SciencePairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('science_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='science_1', to='assets.science')),
                ('science_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='science_2', to='assets.science')),
            ],
            options={
                'verbose_name': 'Fanlar blogi',
                'verbose_name_plural': 'Fanlar bloglari',
                'unique_together': {('science_1', 'science_2')},
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.CharField(max_length=400)),
                ('study_code', models.CharField(max_length=15)),
                ('sciencePair', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.sciencepairs')),
            ],
            options={
                'verbose_name': "Yo'nalish",
                'verbose_name_plural': "Yo'nalishlar",
            },
        ),
        migrations.CreateModel(
            name='StudyInUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant_ball', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('contract_ball', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('grant_count', models.IntegerField(blank=True, default=0)),
                ('contract_count', models.IntegerField(blank=True, default=0)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.study')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.university')),
            ],
            options={
                'verbose_name': "Universitet yo'nalishi",
                'verbose_name_plural': "Universitet yo'nalishlari",
            },
        ),
        migrations.CreateModel(
            name='ImportantSciencePairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('science_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Fan_1', to='assets.science')),
                ('science_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Fan_2', to='assets.science')),
                ('science_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Fan_3', to='assets.science')),
            ],
            options={
                'verbose_name': 'Majburiy fanlar blogi',
                'verbose_name_plural': 'Majburiy fanlar blogi',
                'unique_together': {('science_1', 'science_2', 'science_3')},
            },
        ),
    ]
