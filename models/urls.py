from django.urls import path

from . import views


app_name = 'model_of_phone'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:phone_name>/', views.model_of_phone, name='shell'),
    path('detail/<int:pk>', views.image_of_phone, name='image_of_phone')
]
