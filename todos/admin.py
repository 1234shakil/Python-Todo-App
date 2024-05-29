from django.contrib import admin
from .models import  ParsonalTodo
# Register your models here.


class ParsonalTodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'complate', 'listtime', 'createDate')
  list_filter = ('title', 'complate', 'createDate') 

admin.site.register(ParsonalTodo, ParsonalTodoAdmin)



