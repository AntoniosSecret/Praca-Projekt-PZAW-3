# Generated by Django 5.2 on 2025-04-19 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gainztrackr', '0002_rename_video_url_allexercises_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muscles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='allexercises',
            name='target_muscle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gainztrackr.muscles'),
        ),
    ]
