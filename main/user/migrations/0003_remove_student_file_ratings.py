# Generated by Django 4.0.5 on 2022-07-25 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_student_file_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file_ratings',
        ),
    ]