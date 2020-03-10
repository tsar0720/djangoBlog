from django.db import models

# Create your models here.

class Category(models.Model):
    """ Модель категорий Таблица категорий БД """
    name = models.CharField(verbose_name = "Имя", max_length = 100)
    slug = models.SlugField("url", max_length = 100)

    def __str__(self): # возвращаем имя категории для корректного отображения Category type
        return self.name

    class Meta:  # Указатель корректное отображение
        verbose_name = "Категория" # НА русском языке
        verbose_name_plural = "Категории" # Убираем S вконце

