# Generated by Django 5.0.3 on 2024-04-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_post_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="value",
            field=models.TextField(max_length=100, unique=True),
        ),
    ]