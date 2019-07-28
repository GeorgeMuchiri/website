from django.contrib import admin
from .models import Teacher, Category, Sermon

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'date_created', 'category')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Teacher)
admin.site.register(Sermon, SermonAdmin)
admin.site.register(Category, CategoryAdmin)
