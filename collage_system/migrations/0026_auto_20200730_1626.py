# Generated by Django 3.0.6 on 2020-07-30 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0025_auto_20200730_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses_files',
            old_name='file_name',
            new_name='lecture_name',
        ),
        migrations.RenameField(
            model_name='courses_files',
            old_name='file',
            new_name='lecture_url',
        ),
    ]
