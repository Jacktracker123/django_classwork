from django.shortcuts import render
from . models import *
from . forms import *
# Create your views here.
def index(request):
    context={} #defining an empty dictionary
    # passing form class to an object
    form=Todo_form() 
    if 'save' in request.POST:
     
        key=request.POST.get('save')
        if not key:
            form=Todo_form(request.POST) #fetching data from the textbox
        else:
            todo=Todo.objects.get(id=key)
            form=Todo_form(request.POST,instance=todo)
            
       
        form.save() #adding data to table
        form=Todo_form()

    elif'delete' in request.POST:
        key=request.POST.get('delete')
        todo=Todo.objects.get(id=key) #passing id data from the table to an object
        todo.delete()


    elif'edit' in request.POST:
        key=request.POST.get('edit')
        todo=Todo.objects.get(id=key)
        print(todo)
        form=Todo_form(instance=todo)
    else:
        form=Todo_form()
        


    todo=Todo.objects.all() #passing complete data from the table to an object
    context['todo']=todo #adding values to dictionary
    context['form']=form
    return render(request,'index.html',context)#rendering and passing values to the frontend
