# Generated by Django 3.2.6 on 2023-09-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.TextField(),
        ),
    ]
