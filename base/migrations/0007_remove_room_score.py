# Generated by Django 4.0.5 on 2022-06-02 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_room_rating_room_score_delete_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='score',
        ),
    ]
