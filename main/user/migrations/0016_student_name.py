# Generated by Django 4.0.5 on 2022-07-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_studentgroup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]