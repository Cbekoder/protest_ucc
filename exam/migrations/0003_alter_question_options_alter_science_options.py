# Generated by Django 5.0.6 on 2024-05-22 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_option_is_correct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Savol', 'verbose_name_plural': 'Savollar'},
        ),
        migrations.AlterModelOptions(
            name='science',
            options={'verbose_name': 'Fan', 'verbose_name_plural': 'Fanlar'},
        ),
    ]