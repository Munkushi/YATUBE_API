# Generated by Django 2.2.16 on 2022-02-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220223_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='author',
        ),
    ]