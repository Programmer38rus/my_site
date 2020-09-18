from django.shortcuts import render
from p_library.models import Author, Book
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def books_list(request):
    list = []
    books = Book.objects.all()
    for i in books:
       list.append(i.title) 
    return HttpResponse(list)

def index(request):
    book_max_price = 0
    book_min_price = 0
    book_min = None 

    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()

    new = sum([book.price for book in books if book.copy_count > 1])

    for book in books:
        if book.price > book_max_price:
            book_max_price = book.price
    book_min_price = book_max_price
    for book in books:
        if book.price < book_min_price:
            book_min_price = book.price
            book_min = book

    list_num = [i for i in range(1, 101)]
    biblio_data = {
        "title": "мою библиотеку", 
        "books": books,
        "list_num": list_num,
        "book_max_price": book_max_price,
        "book_min": book_min,
        "book_summ_if": new,
        }

    return HttpResponse(template.render(biblio_data))