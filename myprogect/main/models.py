from django.db import models

# Create your models here.
class Feedback(models.Model):
    # создаем модель. Данные попадают в базу данных. models.Model - стандартное наследование
    # имена переменных буду именами столбцов в тиблице бд.

    # создаем ВЫПАДАЮЩИЙ список

    CITY_CHOICES = (
        ('minsk', 'Минск'),
        ('mogilev', 'Могилев'),
        ('grodno', 'Гродно'),
        ('gomel', 'Гомель'),
    )

    name = models.CharField('Имя', max_length=20)  # Поле ограниченное 255 символов.(можно указать макдлинну самом но < 255)
    email = models.EmailField('Почта', help_text='только почта яндекса') # Поле E-mail. Проверяет правильность ввода мыла
    message = models.TextField('Сообщение') # Поле с неограниченным числом символов.(Макс длинну можно ограничить самому)
    city = models.CharField('Город', max_length=20, choices=CITY_CHOICES) # выпадающий список

    class Meta:
        # класс для локализации на русский язык

        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

# для того чтобы модель появилась в бд надо сделать 1 - миграцию, 2 - созданый модель перенести в бд
# миграция - в терминале прописывыем >>>python mange.py makemigrations
# ПОСЛЕ миграции создаем модель в бд. в CMD пишем >>> python mange.py migrate

    def __str__(self):
        return self.email

    # создаем модель "новости"
class News(models.Model):

    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст новости')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title