# Generated by Django 4.0.5 on 2022-07-18 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_homeworksubmission_is_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworksubmission',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='courses.homework'),
        ),
    ]
