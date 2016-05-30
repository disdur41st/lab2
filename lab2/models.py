from django.db import models

class LibraryEmployee(models.Model):
    name = models.CharField(max_length=30)
    patronymic_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    position = models.CharField(max_length=30)

class Reader(models.Model):
    library_card_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    patronymic_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    passport_number = models.IntegerField()
    date_of_birth = models.DateField()
    grop_number = models.IntegerField()

class Operation(models.Model):
    book_copy = models.ForeignKey('BookCopy')
    library_card_number= models.ForeignKey('Reader')
    library_employee = models.ForeignKey('LibraryEmployee')
    operation_date = models.DateField()
    required_return_date = models.DateField()

class BookCopy(models.Model):
    name = models.CharField(max_length=30)
    year_of_publication = models.IntegerField() 

class Author(models.Model):
    name = models.CharField(max_length=30)
    patronymic_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    book_copy = models.ManyToManyField(BookCopy)
