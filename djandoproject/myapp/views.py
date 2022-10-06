from django.http import HttpResponse
from .models import Projects, Task
from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Djando course!!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username = 'loncho'
    return render(request, 'about.html', {
        'username': username
    })
def projects(request):
    #projects = list(Projects.objects.values())
    projects = Projects.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = get_object_or_404(Task, title = title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })