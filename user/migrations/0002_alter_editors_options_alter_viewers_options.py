# Generated by Django 4.2.7 on 2024-02-01 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editors',
            options={'verbose_name_plural': 'Editors'},
        ),
        migrations.AlterModelOptions(
            name='viewers',
            options={'verbose_name_plural': 'Viewers'},
        ),
    ]
