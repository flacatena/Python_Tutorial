from django.urls import path
from . import views

urlpatterns = [
    path('objectives_list', views.objectives_list, name='objectives_list'),
    path('',views.django_intro, name='django_intro'),
    path('instructions-list/<int:id>', views.instructions_list, name='instructions_list'),
    path('hello_world', views.hello_world, name='hello_world'),
    path('what_django', views.what_django, name='what_django'),
    path('model_intro', views.model_intro, name="model_intro"),
    path('views_intro', views.views_intro, name='views_intro'),
    path('template_intro',views.template_intro, name='template_intro'),
    path('urls_intro', views.urls_intro, name='urls_intro'),
    path('summarize_stages',views.summarize_stages, name='summarize_stages'),   
]