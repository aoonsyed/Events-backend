# Generated by Django 5.1.2 on 2024-10-17 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Role',
            new_name='role',
        ),
    ]
