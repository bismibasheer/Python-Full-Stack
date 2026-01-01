from django.contrib import admin
from manager.models import Author, Category

# Register your models here.
admin.site.register(Author)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['Category']
    prepopulated_fields={"slug":["Category",]}

admin.site.register(Category,CategoryAdmin)    
