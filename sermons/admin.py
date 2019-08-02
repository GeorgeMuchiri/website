from django.contrib import admin
from .models import Teacher, Category, Sermon, Messages

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'date_created', 'category')

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message', 'name', 'email')


admin.site.register(Teacher)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Sermon, SermonAdmin)
admin.site.register(Category, CategoryAdmin)
