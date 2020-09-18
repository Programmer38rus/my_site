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
    dict_author = {}

    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()

    books_no_ru = sum([book.price*book.copy_count for book in books if book.author.country != "RU"])
    books_pushkin = sum([book.price*book.copy_count for book in books if book.author.full_name == "Пушкин Александр Сергеевич"])
    books_duglas = sum([book.price for book in books if book.author.full_name == "Douglas Adams"])
    books_not_one = sum([book.price*book.copy_count for book in books if book.copy_count != 1])

    new = sum([book.price for book in books if book.copy_count > 1])

    for book in books:

        if book.price > book_max_price:
            book_max_price = book.price
        dict_author[book.author.full_name] = book.price * book.copy_count    

    max_all_price = sum([v for k, v in dict_author.items()])
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
        "vot": dict_author,
        "vot2": books_no_ru,
        "vot3": books_pushkin, 
        "vot4": books_duglas,
        "vot5": books_not_one,
        }

    return HttpResponse(template.render(biblio_data))