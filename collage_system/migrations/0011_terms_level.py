# Generated by Django 3.0.6 on 2020-07-25 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0010_level_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='terms',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collage_system.Level'),
        ),
    ]
