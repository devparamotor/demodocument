# Generated by Django 3.2.7 on 2021-09-14 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydocument', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdoc',
            old_name='user_id',
            new_name='user_name',
        ),
    ]