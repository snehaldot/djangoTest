from django.db import models
from django.contrib import admin
# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website =models.URLField()

    def __unicode__(self):
        return self.name

class Auther(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    
    def __unicode__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authers = models.ManyToManyField(Auther)
    publisher=models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','address', 'city', 'state_province', 'country','website']
    search_fields = ['name']
    list_filter = ['name']

class AutherAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']
    search_fields = ['first name']
    list_filter = ['first_name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher' ,'publication_date']
    search_fields = ['title']
    list_filter = ['publication_date']
    date_hierarchy = 'publication_date'
    ordering = ['publication_date',] # Add ['-publication_date'] for decending order....
   # fields = ['title','publisher','publication_date']
    filter_horizontal = ['authers']
   # filter_vertical = ['authers']
    raw_id_fields = ['publisher']
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Auther, AutherAdmin)
admin.site.register(Book, BookAdmin)








