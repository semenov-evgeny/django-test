from django.http import HttpResponse


#def index(request):
    # создаём объект типа HttpResponse
#    resp = HttpResponse('<h1>Главная страница проекта My Praktikum Blog</h1> ссылка на анфису <a href="/anfisa/about">тут</a>')
    # и возвращаем его
#    return resp

def about(request):
    return render(request, 'templates/about.html')
