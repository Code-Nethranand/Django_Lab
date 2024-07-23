# Generated by Django 5.0.6 on 2024-07-09 12:02

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
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('code', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
                ('fees', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('usn', models.TextField(max_length=50)),
                ('proj', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('sec', models.TextField(max_length=50)),
                ('usn', models.TextField()),
                ('cgpa', models.FloatField()),
            ],
        ),
    ]
