# Generated by Django 4.0.3 on 2022-03-21 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0002_remove_comments_is_active_like_pin_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='pin',
            field=models.ForeignKey(default='ff3f4d5b-c4e1-4126-8ff5-b95e1da6aaa5', on_delete=django.db.models.deletion.CASCADE, to='pins.pin'),
            preserve_default=False,
        ),
    ]