from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    start_date = models.DateField(auto_now_add=True, verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    description = models.CharField(max_length=200, verbose_name='Description')

    def __str__(self):
        return self.name