from django.contrib import admin

# Register your models here.
from main.models import Lists, Tasks


@admin.register(Lists)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'created', 'due', 'owner', 'mark', ]
    ordering = ['created', 'due']
    search_fields = ['task', 'owner', ]
    list_filter = ['created', 'due', 'mark']
    list_editable = ['mark', 'due']
    list_per_page = 5
