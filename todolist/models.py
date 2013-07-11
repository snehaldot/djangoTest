from django.db import models
from django.contrib import admin
# Create your models here.

class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.datetime)

class TodoItem(models.Model):
    name = models.CharField(max_length=60)
    created = models.ForeignKey(DateTime)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["name","priority","difficulty","created","done"]
    search_field = ["name"]

class ItemInline(admin.TabularInline):
    model = TodoItem

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemInline]

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(DateTime, DateAdmin)
