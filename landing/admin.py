from django.contrib import admin
from .models import *

# Register your models here.

#для отображения,напр., двух полей на сервере
class SubscriberAdmin (admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name',]
    search_fields = ['name', 'email']

    fields = ["email"]
    #exclude = ["email"]
    #list_filter = ['name',]
    #search_fields = ['name', 'email']
    #inlines = [FieldMappingInline]
    #fields = ["email"]


    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
