# Generated by Django 4.0.5 on 2022-07-14 10:38

import courses.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('homework_title', models.CharField(max_length=255)),
                ('homework_text', models.TextField(blank=True)),
                ('homework_file', models.FileField(upload_to='homeworks/questions/group/')),
                ('homework_created_time', models.DateTimeField(auto_now_add=True)),
                ('homework_deadline_time', models.DateTimeField(null=True, validators=[courses.models.deadline_time])),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.student')),
                ('student_group', models.ManyToManyField(to='user.studentgroup')),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='user.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeworkSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('upload_homework_time', models.DateTimeField(auto_now_add=True)),
                ('submission_homework_file', models.FileField(blank=True, upload_to='homeworks/answers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'ppt'])])),
                ('submission_rating', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
