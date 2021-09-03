from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Feedback) # регистрация модели
admin.site.register(News)