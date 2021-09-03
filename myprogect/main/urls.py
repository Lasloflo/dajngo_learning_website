from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('news', news),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail') # генератор для каждой новости. Генерирует первичный ключ
]                                                     #  name(обязательный) - позволяет ссылку вставлять в конкретное место