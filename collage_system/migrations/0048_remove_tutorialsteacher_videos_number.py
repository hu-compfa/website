# Generated by Django 3.0.6 on 2020-10-10 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0047_auto_20201009_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialsteacher',
            name='videos_number',
        ),
    ]
