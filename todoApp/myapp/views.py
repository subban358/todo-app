from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ToDo

def index(request):
	tasks = ToDo.objects.all().order_by("-time")

	return render(request, "index.html",{'tasks' : tasks})

def addTask(request):
	if request.method == 'POST':
		curr = timezone.now()
		task = request.POST['task']
		print(task)
		obj = ToDo.objects.create(task = task, time = curr)
		obj.save()
	return redirect('/')	

def delete(request, todo_id):
	ToDo.objects.get(id=todo_id).delete()
	return redirect('/')