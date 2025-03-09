from django.contrib import admin

from core.models import *

class courseAdmin(admin.ModelAdmin):
    list_display = ['name','image','id']


# Register your models here.
admin.site.register(course, courseAdmin)
admin.site.register(contact)
admin.site.register(category)
admin.site.register(apply)
