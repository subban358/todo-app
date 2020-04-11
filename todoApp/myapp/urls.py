from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name ='index'),
	path('addTask',views.addTask, name = 'addTask'),
	path('delete/<int:todo_id>/',views.delete, name = 'delete')
]