# Generated by Django 2.1.5 on 2020-07-11 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
    ]
