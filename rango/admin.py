from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)



# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','url')

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)