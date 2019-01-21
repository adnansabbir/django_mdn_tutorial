from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

# Register your models here.
