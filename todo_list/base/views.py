from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List
# Create your views here.
def index(request):
    item_in_list = List.objects.all()
    
    return render(request,'face/index.html',{"item_in_list": item_in_list})


def create(request):
    if request.method =="POST":
        new_item = request.POST.get('item_name')
        List.objects.create(item=new_item)
        return redirect('index')
        
    return render(request,'face/create.html')

def delete(request):
    item = List.objects.all()
    if request.method=="POST":
        delete_item = request.POST.get('delete_items')
        List.objects.filter(item=delete_item).delete()
        return redirect('index')
    return render(request,'face/delete.html',{"item": item})

# Work for future connor figure out how to get the value of the item in the List
# model and pass it into the return statement and then have that loop
# which does each of the items and puts them in a list. 


