# Generated by Django 3.1.4 on 2020-12-07 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=2000)),
                ('complexity', models.CharField(choices=[('S', 'Simple'), ('M', 'Medium'), ('D', 'Difficult')], max_length=30)),
                ('options', models.CharField(max_length=1000)),
                ('correct_answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=8)),
                ('assessment_count', models.IntegerField(default=0)),
                ('last_assessment_score', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_number', models.IntegerField(default=1)),
                ('score', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
        ),
    ]
