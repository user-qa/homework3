from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=50)
    year_written = models.IntegerField()