from django.contrib import admin
from FirstApp.models import Blogger, Entry
# Register your models here.


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email')
#     search_fields = ('first_name', 'last_name')

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'publisher', 'publication_date')
#     list_filter = ('publication_date',)
#     date_hierarchy = 'publication_date'
#     ordering = ('-publication_date',)
#     filter_horizontal = ('authors',)
#     raw_id_fields = ('publisher',)

class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ['name']

# class EntryAdmin(admin.ModelAdmin):
#     list_display = ('author', 'headline', 'pub_date')
#     search_fields = ('author', 'headline', 'pub_date')
#     list_filter = ['pub_date']
#     ordering = ('-pub_date',)
#     #raw_id_fields = ('author')

# admin.site.register(Publisher)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
admin.site.register(Blogger, BloggerAdmin)
#admin.site.register(Entry, EntryAdmin)
