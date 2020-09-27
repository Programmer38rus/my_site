from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    # @staticmethod
    # def publishing_house_name(obj):
    #     return obj.publishing_house.full_name

    list_display = ('title', 'author_full_name', 'publishing_house')
    fields = (('title', 'description'), 'year_release', 'author', 'price', 'publishing_house')
    exclude = ('ISBN',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PubHouseAdmin(admin.ModelAdmin):
    list_display=('full_name', 'count_book')
    list_filter=('full_name',)
    # fields = (('full_name', 'count_book'), )
    