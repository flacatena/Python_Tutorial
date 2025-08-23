from django.shortcuts import render
from . models import Objectives , Instructions

def objectives_list(request):
    objectives_list = Objectives.objects.exclude(objective_description= "Hello World")
    return render(request, 'DjangoTutorial/objectives_list.html',{'objectives': objectives_list})

def instructions_list(request,id):
    objective_id = Objectives.objects.get(id = id)
    instructions_list = Instructions.objects.filter(objective = id)
    return render(request, 'DjangoTutorial/instructions_list.html',{'instructions': instructions_list ,'objective_id':objective_id})

def hello_world(request):
    hello_world = Objectives.objects.get(objective_description="Hello World")
    hello_world_instructions = Instructions.objects.filter(objective = hello_world)
    return render(request, 'DjangoTutorial/hello_world.html',{'instructions': hello_world_instructions , 'objective_id' : hello_world})

def django_intro(request):
    return render(request,'DjangoTutorial/django_intro.html')

def what_django(request):
    return render(request, 'DjangoTutorial/what_django.html')

def model_intro(request):
    return render(request, 'DjangoTutorial/model_intro.html')

def views_intro(request):
    return render(request, 'DjangoTutorial/views_intro.html')

def template_intro(request):
    return render(request, 'DjangoTutorial/template_intro.html')

def urls_intro(request):
    return render(request, 'DjangoTutorial/urls_intro.html')

def summarize_stages(request):
    return render(request, 'DjangoTutorial/summarize_stages.html')

def components_indepth(request):
    return render(request, 'DjangoTutorial/components_indepth.html')

def url_indepth(request):
    return render(request, 'DjangoTutorial/url_indepth.html')

