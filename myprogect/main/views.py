from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import *  # импортируем модель для отображения на экране данных из бд
from django.views.generic import DetailView # класс который позволяет проводить генерацию для каждой новости в отдельности
# Create your views here.

def contact(request):
    return render(request, 'main/index.html')

def index(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('contact')

    feedbacks = Feedback.objects.all()   # для просмотра на экране данных из бд. Создаем переменную
    form = FeedbackForm()
    data = {
        'form': form,
        'feedbacks': feedbacks
    }
    return render(request, 'main/index.html', data) #возвращает index.html из tempaltes/main

class NewsDetailView(DetailView):
    # класс для отобрадения каждой новости в отдельной модели

    model = News  # переменная model говорит на основании какой модели все будет происходить
    template_name = 'main/news_detail.html'  # какой шаблон используется для каждой новости
    context_object_name = 'news'  # к какому имени я буду обращаться при генерации

def news(request):
    # шаблон для страницы news

    news = News.objects.all()  # объект всех новостей
    data = {                    # по ключу будет отображаться на странице
        'news': news
    }
    return render(request, 'main/news.html', data)
