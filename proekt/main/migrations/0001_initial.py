# Generated by Django 5.0.3 on 2024-03-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.IntegerField(verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=200, verbose_name='Ответ')),
                ('date', models.DateTimeField(verbose_name='Дата ответа')),
            ],
        ),
    ]