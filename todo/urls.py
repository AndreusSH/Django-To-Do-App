from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addToDo, name='add'),
    path('checked/<id>', views.taskCompleted, name='checked'),
    path('deleteCompleted', views.deleteTasksCompleted, name='deleteCompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll'),



]
