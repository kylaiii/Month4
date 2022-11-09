from django.db import models

# Create your models here.

class Director(models.Model):
    class Meta:
        verbose_name = 'Режиссера'
        verbose_name_plural = 'Режиссеры'
    name = models.CharField(max_length=200)



    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=250, null=True)
    rating = models.FloatField(default=0, blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE )
    pages = models.ImageField(blank=True)

    def __str__(self):
        return self.name






