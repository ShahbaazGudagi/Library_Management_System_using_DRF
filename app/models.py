from unicodedata import category
from django.db import models

# Create your models here.
class BooksCategory(models.Model):
    Category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.Category_name
    

class Books(models.Model):
    book_name=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50)
    books_category=models.ForeignKey(BooksCategory, on_delete=models.CASCADE,related_name='BooksCategory')
    books_quantity=models.IntegerField()

    def __str__(self):
        return self.book_name
    