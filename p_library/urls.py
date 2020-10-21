from django.contrib import admin
from django.urls import path
from .views import AuthorEdit, AuthorList, books_author_create_many, AuthorUpdate, AuthorDelete, HomePageView, \
    PublisherList, PublisherList3, TestFormView

app_name = 'p_library'

urlpatterns = [
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorUpdate.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
    # path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_author_create_many, name='books_author_create_many'),
    path('class_test', HomePageView.as_view()),
    path('publisher', PublisherList.as_view()),
    # path('<name:name>/', PublisherList3.as_view(), name="publisher-detail"),
    path('test_form', TestFormView.as_view()),
]
