from django.shortcuts import render
from lab2.models import LibraryEmployee
from lab2.models import Reader
from lab2.models import Operation
from lab2.models import BookCopy
from lab2.models import Author
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    LibraryEmployee.objects.create (id = 1, name = "Иван", patronymic_name = "Сергеевич", surname = "Кочин",
                                    position = "секретарь")
    LibraryEmployee.objects.create (id = 2, name = "Фёдор", patronymic_name = "Петрович", surname = "Мерков",
                                    position = "библиотекарь")
    LibraryEmployee.objects.create (id = 3, name = "Лариса", patronymic_name = "Константиновна", surname = "Никифорова",
                                    position = "библиотекарь")

    
    Reader.objects.create (id = 1, library_card_number = "5946354869", name = "Алексей", patronymic_name = "Петрович", surname = "Фандорин",
                                    passport_number = "1568735195", date_of_birth = "1984-10-12", proup_number = "562")
    Reader.objects.create (id = 2, library_card_number = "5948351684", name = "Аркадий", patronymic_name = "Львович", surname = "Ночин",
                                    passport_number = "1368495362", date_of_birth = "1965-05-02", proup_number = "469")
    Reader.objects.create (id = 3, library_card_number = "4962384679", name = "Августин", patronymic_name = "Эрнестович", surname = "Зубрин",
                                    passport_number = "5316792645", date_of_birth = "1990-05-22", proup_number = "163")


    Operation.objects.create (id = 1, operation_date = "2013-11-19", required_return_date = "2014-05-19", operation_type = "выдача")
    Operation.objects.create (id = 2, operation_date = "2013-12-25", required_return_date = "2014-06-25", operation_type = "выдача")
    Operation.objects.create (id = 3, operation_date = "2014-03-05", required_return_date = "2014-10-05", operation_type = "выдача")

    
    BookCopy.objects.create (id = 1, name = "Beatles' songbook", year_of_publication = "1985", amount_of_all_copies = "2")
    BookCopy.objects.create (id = 2, name = "Общий курс физики", year_of_publication = "2003", amount_of_all_copies = "20")
    BookCopy.objects.create (id = 3, name = "Прикладная философия", year_of_publication = "1999", amount_of_all_copies = "15")


    Author.objects.create (id = 1, name = "Sergio", patronymic_name = "Сергеевич", surname = "Palumbo", book_copy = '1')
    Author.objects.create (id = 2, name = "Очень", patronymic_name = "Плохой", surname = "Писатель", book_copy = '2')
    Author.objects.create (id = 3, name = "Виктор", patronymic_name = "Антонович", surname = "Розгунов", book_copy = '3')









    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'employees_list' : LibraryEmployee.objects.all(),   
                'readers_list' : Reader.objects.all(),
                'operations_list' : Operation.objects.all(),
                'book_copies_list' : BookCopy.objects.all(),
                'authors_list' : Author.objects.all()            
            }
        )
        return context
