from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, name):
    ls = ToDoList.objects.get(id=1)
    item = ls.item_set.create(text = name, complete=False)
    return HttpResponse("test successful! %s " % item)