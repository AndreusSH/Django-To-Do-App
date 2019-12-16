# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.http import require_POST
from .models import MyForm
from .forms import AddTask
# Create your views here.

def index(request):
    to_do = MyForm.objects.order_by('id')
    form = AddTask()
    context = {'to_do' : to_do, 'form' : form}
    return render(request, 'todo.html', context)

@require_POST
def addToDo(request):
    form = AddTask(request.POST)
    #add to the database what I input
    if form.is_valid():
        new_to_do = MyForm(text = request.POST['text'])
        new_to_do.save()
    # print(request.POST['text'])
    #I am redirected again to the index page
    return redirect('index')

def taskCompleted(request, id):
    to_do_checked = MyForm.objects.get(pk=id)#I retrieve a specific task
    to_do_checked.complete = True
    to_do_checked.save()
    return redirect('index')

def deleteTasksCompleted(request):
    MyForm.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    MyForm.objects.all().delete()
    return redirect('index')


