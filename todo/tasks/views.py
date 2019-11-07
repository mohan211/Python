from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasklist

def index(request):
	tasks = Tasklist.objects.all()
	context = {'tasks': tasks}
	return render(request, 'index.html', context)

def detail(request, id):
	task=Tasklist.objects.get(id=id)
	context={'task':task}
	return render(request, 'detail.html', context)

def addtask(request):
	if request.method == 'POST':
		title=request.POST['title']
		text=request.POST['text']
		newtask=Tasklist(title=title, text=text)
		newtask.save()
		return redirect('/tasks')
	else:
		return render(request, 'add.html')

def delete(request, id):
	dtask=Tasklist.objects.get(id=id)
	dtask.delete()
	return redirect('/tasks')


