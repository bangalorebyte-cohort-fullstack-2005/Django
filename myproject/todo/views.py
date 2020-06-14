from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data['title']
            text= form.cleaned_data['text']
            print("formdata",title,text)
            obj = Todo(title=title, text=text)
            obj.save()
            return redirect('/todo/index')
    context = {'todos':todos,'form':form} 
    return render(request,'todo/index.html',context)

def update(request,id):
    if request.method == 'GET':
        data1 = Todo.objects.get(id=id)
        print(data1)
        context = {'todo':data1}
        return render(request, 'todo/update.html',context)
    else:
        title=request.POST['title']
        text = request.POST['text']
        Todo.objects.filter(id=id).update(title=title,text=text)

        return redirect("/todo/index")

def delete(request,id):
    if request.method == 'GET':
        Todo.objects.filter(id=id).delete()
    return redirect("index")