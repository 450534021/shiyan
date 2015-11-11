

# Register your models here.
from django.contrib import admin
from mytest.models import Book,Author

class BookAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Book)
admin.site.register(Author)
