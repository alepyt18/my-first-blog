from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('rota/', views.post_rota, name='post_rota')
]