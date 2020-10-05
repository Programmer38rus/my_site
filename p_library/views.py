from django.shortcuts import render
from p_library.models import Author, Book, PublishingHouse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


# Create your views here.
def books_list(request):
    list = []
    books = Book.objects.all()
    for i in books:
        list.append(i.title)
    return HttpResponse(list)


def publishing_house(request):
    template = loader.get_template('publishinghouse.html')

    pub_houses = PublishingHouse.objects.all()

    data = {
        "pub_houses": pub_houses
    }
    return HttpResponse(template.render(data, request))


def index(request):
    book_max_price = 0
    book_min_price = 0
    book_min = None
    dict_author = {}

    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()

    # pub_houses = PublishingHouse.objects.all()
    books_no_ru = 0
    books_pushkin = 0
    books_duglas = 0
    books_not_one = 0
    new = 0

    for book in books:
        if book.author.country != "RU":
            books_no_ru += book.price * book.copy_count
        if book.author.full_name == "Пушкин Александр Сергеевич":
            books_pushkin += book.price * book.copy_count
        if book.author.full_name == "Douglas Adams":
            books_duglas += book.price
        if book.copy_count != 1:
            books_not_one += book.price * book.copy_count
        if book.copy_count > 1:
            new += book.price

    # books_no_ru = sum([book.price*book.copy_count for book in books if book.author.country != "RU"])
    # books_pushkin = sum([book.price*book.copy_count for book in books if book.author.full_name == "Пушкин Александр Сергеевич"])
    # books_duglas = sum([book.price for book in books if book.author.full_name == "Douglas Adams"])
    # books_not_one = sum([book.price*book.copy_count for book in books if book.copy_count != 1])

    # new = sum([book.price for book in books if book.copy_count > 1])

    # вычисляем максимальну и минимальную стоимость книги.
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
        "force": [1, 2, 3, 4, 5],
        "pub_houses": pub_houses,
    }

    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')

            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')
