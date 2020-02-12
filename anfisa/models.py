from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    # models.Model означает, что объект Post является моделью Django и должен сохранить в его базу данных 
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ссылка на другую модель
    title = models.CharField(max_length=200)
    # определили текстовое после с ограничением по количеству символов
    text = models.TextField()
    # поле неограниченное для длинногот текста
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.noe()
        self.save

    def __str__(self):
        return self.title


