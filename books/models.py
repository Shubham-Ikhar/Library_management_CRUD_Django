from django.db import models

# Create your models here.
class Books(models.Model):
    author_name = models.CharField(max_length=70)
    book_name = models.CharField(max_length=70)
