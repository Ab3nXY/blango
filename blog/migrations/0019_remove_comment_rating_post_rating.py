# Generated by Django 5.0.4 on 2024-05-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_comment_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=3.0),
        ),
    ]
