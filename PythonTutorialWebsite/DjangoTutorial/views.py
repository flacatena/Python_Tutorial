from django.shortcuts import render
from . models import Objectives , Instructions

def objectives_list(request):
    objectives_list = Objectives.objects.all()
    return render(request, 'DjangoTutorial/objectives/objectives_list.html',{'objectives': objectives_list})

def instructions_list(request,id):
    objective_id = Objectives.objects.get(id = id)
    instructions_list = Instructions.objects.filter(objective = id)
    return render(request, 'DjangoTutorial/instructions/instructions_list.html',{'instructions': instructions_list ,'objective_id':objective_id})
