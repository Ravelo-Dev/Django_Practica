from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Project!!'
    return render(request, 'index.html', {
        'title': title
        })

def about(request):
    username = 'Ravelo-Dev'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    return HttpResponse("Hello %s" % username)


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })
    #Devolver .json a la pagina
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)

def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
        })
    # tasks = Tasks.objects.get(id=id)
    # buscar tarea por nombre suponiendo que el parametro sea titulo o title:
    # tasks = Tasks.objects.get(title=title)
    """tasks = get_object_or_404(Tasks, id=id)
    return HttpResponse("Tasks: %s" % tasks.title)"""

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', 
                    {'form': CreateNewTask()})  
    else:
        Tasks.objects.create(title=request.POST['title'], 
                            description=request.POST['description'], project_id=1)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', 
                  {'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
        
        # return render(request, 'projects/create_project.html', 
                  #{'form': CreateNewProject})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', 
                  {'project': project,
                  'tasks': tasks})
        
          

