# Generated by Django 5.1.1 on 2024-09-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
