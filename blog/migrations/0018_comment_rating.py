# Generated by Django 5.0.4 on 2024-05-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comment_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.FloatField(default=3.0),
        ),
    ]