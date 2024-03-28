# Generated by Django 5.0.3 on 2024-03-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_response_delete_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='question1',
            field=models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2')], max_length=200),
        ),
        migrations.AlterField(
            model_name='response',
            name='question2',
            field=models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2')], max_length=200),
        ),
    ]