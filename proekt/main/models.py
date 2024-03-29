from django.db import models


class Response(models.Model):
    QUESTION1_CHOICES = [
        ('option1', '«Иван-царевич и Серый волк»'),
        ('option2', '«Царевна-лягушка»'),
        ('option3', '«Сказка о царе Салтане»'),
    ]
    question1 = models.CharField(max_length=200, choices=QUESTION1_CHOICES)
    QUESTION2_CHOICES = [
        ('option1', '«Судьба человека»'),
        ('option2', '«Война и мир»'),
        ('option2', '«Сын полка»'),
    ]
    question2 = models.CharField(max_length=200, choices=QUESTION2_CHOICES)