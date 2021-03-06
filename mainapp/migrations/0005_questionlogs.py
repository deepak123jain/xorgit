# Generated by Django 3.1.4 on 2020-12-09 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_qalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('DateTime', models.DateTimeField(auto_now=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.allsubjectques')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
        ),
    ]
