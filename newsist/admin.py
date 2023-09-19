from django.contrib import admin
from .models import Admins, News

# Register your models here.
admin.site.register(Admins)
admin.site.register(News)