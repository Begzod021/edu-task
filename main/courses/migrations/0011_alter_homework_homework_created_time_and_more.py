# Generated by Django 4.0.5 on 2022-07-21 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('courses', '0010_remove_homework_student_group_homework_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='homework_created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='homeworksubmission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answer_student', to='user.student'),
        ),
    ]
