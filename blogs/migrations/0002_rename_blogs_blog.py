# Generated by Django 5.1.1 on 2024-09-05 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='Blog',
        ),
    ]
