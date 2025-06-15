from django.urls import path
from . import views

urlpatterns = [
    path('', views.objectives_list, name='objectives_list'),
    path('instructions-list/<int:id>', views.instructions_list, name='instructions_list'),
    
]