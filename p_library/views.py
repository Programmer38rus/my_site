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
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    list_num = [i for i in range(1, 101)]
    biblio_data = {
        "title": "мою библиотеку", 
        "books": books,
        "list_num": list_num,
        }

    return HttpResponse(template.render(biblio_data))