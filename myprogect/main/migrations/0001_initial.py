# Generated by Django 3.2.6 on 2021-08-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('city', models.CharField(choices=[('minsk', 'Минск'), ('mogilev', 'Могилев'), ('grodno', 'Гродно'), ('gomel', 'Гомель')], max_length=20, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
