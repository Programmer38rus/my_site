from django.shortcuts import render
from p_library.models import Author, Book, PublishingHouse, Friend
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect

from p_library.forms import AuthorForm, BookForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, DetailView, FormView
from django.urls import reverse_lazy

from django.forms import formset_factory

# Импортируем class-based views
from django.views.generic.base import TemplateView

# Импорт для PUT запросов
import json

from django.utils import timezone

# Create your views here.

def base_view(request):
    template = loader.get_template('base.html')
    data = {}
    return HttpResponse(template.render(data, request))

def books_author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  # Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  # Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')

        if author_formset.is_valid() or book_formset.is_valid():  # Проверяем, валидны ли данные формы
            for author_form in author_formset:
                author_form.save()  # Сохраним каждую форму в формсете
            for book_form in book_formset:
                book_form.save()  # Сохраним каждую форму в формсете
            return HttpResponseRedirect(
                reverse_lazy('p_library:author_list'))  # После чего, переадресуем браузер на список всех авторов.
    else:  # Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='authors')  # Инициализируем формсет и ниже передаём его в контекст шаблона.
        book_formset = BookFormSet(prefix='books')

    return render(request, 'manage_authors.html', {'author_formset': author_formset,
                                                   # 'book_formset': book_formset
                                                   })

class FriendsList(ListView):
    model = Friend
    context_object_name = 'friends'
    template_name = 'list_friends.html'

class TestFormView(FormView):
    template_name = 'test_form.html'
    form_class = AuthorForm
    success_url = '/authors/'

    def form_valid(self, form):
        form.send_message()
        return super().form_valid(form)

class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    # fields = ['full_name', 'birth_year', 'country']
    template_name = 'author_edit.html'

class AuthorDelete(DeleteView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_delete.html'

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_delete.html'


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
    pub_houses = PublishingHouse.objects.all()
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
        "force_django": [1, 2, 3, 4, 5],
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

class HomePageView(TemplateView):

    template_name = "class-base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["full_name"] = Author.objects.all()
        return context


# Создаем классы Class-base view для публикаций

class PublisherList(ListView):
    model = PublishingHouse
    template_name = 'publishinghouse_list.html'
    paginate_by = 1 # Количество выводов элементов
    def put(self, request):
        data = json.loads(request.body)
        publisher = self.model(**data)
        publisher.save()
    context_object_name = 'new'

class PublisherList2(View):
    model = PublishingHouse

    def get(self):
        publishers_list = self.model.objects.all()
        return publishers_list

    def put(self, request):
        data = json.loads(request.body)
        publisher = self.model(**data)
        publisher.save()

# через DetailView

class PublisherList3(DetailView):
    model = Author
    # context_object_name = "new_name"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context