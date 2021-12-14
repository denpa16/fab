from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    start_date = models.DateField(auto_now_add=True, verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    description = models.CharField(max_length=200, verbose_name='Description')

    def __str__(self):
        return self.name

class Question(models.Model):

    QUESTION_TYPES = (
        ('text_field', 'Ответ текстом'),
        ('radio', 'Один вариант'),
        ('check_boxes', 'Выбор нескольких вариантов'),
    )

    text = models.TextField()
    type_question = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES,
        verbose_name='Тип вопроса',
    )
    poll = models.ForeignKey(
        Poll, blank=True, on_delete=models.CASCADE,
        related_name="questions"
    )

    def __str__(self):
        return self.text