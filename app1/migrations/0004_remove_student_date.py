# Generated by Django 4.1.6 on 2023-02-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
    ]