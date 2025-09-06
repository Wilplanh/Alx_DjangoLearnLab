from django.db import models

class author(models.Model):
    name = models.CharField(max_length=100)
   
class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(author, on_delete=models.CASCADE)

class library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(book)

class librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(library, on_delete=models.CASCADE)

    

# Create your models here.
