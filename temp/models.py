from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    review_text = models.TextField('Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'