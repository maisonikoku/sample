# Generated by Django 4.1.6 on 2023-02-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_student_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stdId',
            field=models.CharField(max_length=10, verbose_name='Student Id'),
        ),
    ]
