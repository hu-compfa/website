# Generated by Django 3.0.6 on 2020-10-30 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0056_auto_20201016_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_pic',
        ),
    ]
