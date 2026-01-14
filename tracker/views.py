#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Tracker index")

def board(request):
    return HttpResponse("There is only one project. Here it is!")

def create(request):
    return HttpResponse("Create a task here!")

def view(request, task_id):
    return HttpResponse(f"Viewing task {task_id}")