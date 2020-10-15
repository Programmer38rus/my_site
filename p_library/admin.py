from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse, Inspiration, Friend

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author

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

@admin.register(Inspiration)
class Inspiration(admin.ModelAdmin):
    pass

@admin.register(Friend)
class Friend(admin.ModelAdmin):
    pass