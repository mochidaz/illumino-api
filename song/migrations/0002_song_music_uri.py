# Generated by Django 5.0.3 on 2024-07-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='music_uri',
            field=models.FileField(null=True, upload_to='song/'),
        ),
    ]
