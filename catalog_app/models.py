from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, **NULLABLE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

