from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")
    search_fields = ("title", "description")
    list_filter = ("completed",)
    
admin.site.register(Task, TaskAdmin)