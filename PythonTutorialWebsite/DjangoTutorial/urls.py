from django.urls import path
from . import views

urlpatterns = [
    path('objectives_list', views.objectives_list, name='objectives_list'),
    path('',views.django_intro, name='django_intro'),
    path('instructions-list/<int:id>', views.instructions_list, name='instructions_list'),
    path('hello_world', views.hello_world, name='hello_world'),
    path('what_django', views.what_django, name='what_django'),
    path('model_intro', views.model_intro, name="model_intro"),
   
]