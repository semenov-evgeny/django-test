from django.http import HttpResponse


def index(request):
    # создаём объект типа HttpResponse
    resp = HttpResponse('<h1>Главная страница проекта My Praktikum Blog</h1>')
    # и возвращаем его
    return resp
