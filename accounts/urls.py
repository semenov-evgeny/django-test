from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.sign_up),
    path('sign-in', views.sign_in),
    path('my-account', views.my_account),
    path('friends/<str:user>', views.get_friends),
]
