# Generated by Django 5.0.3 on 2024-03-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_response_question1_alter_response_question2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='question1',
            field=models.CharField(choices=[('option1', '«Иван-царевич и Серый волк»'), ('option2', 'Царевна-лягушка'), ('option3', 'Сказка о царе Салтане')], max_length=200),
        ),
        migrations.AlterField(
            model_name='response',
            name='question2',
            field=models.CharField(choices=[('option1', 'Судьба человека'), ('option2', 'Война и мир'), ('option2', 'Сын полка')], max_length=200),
        ),
    ]