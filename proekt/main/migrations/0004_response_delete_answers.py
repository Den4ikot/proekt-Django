# Generated by Django 5.0.3 on 2024-03-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_answers_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=200)),
                ('question2', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
