# Generated by Django 5.0.2 on 2024-02-22 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_developer',
            new_name='is_employee',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_manager',
            new_name='is_hr',
        ),
    ]