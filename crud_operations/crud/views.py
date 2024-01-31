from django.shortcuts import render
from . models import *
from . forms import *

# Create your views here.
def index(request):
    context={}
    form=Manage_form()

    if request.method=='POST':
        if'save' in request.POST:
            key=request.POST.get('save')


            if not key:
                form=Manage_form(request.POST)
            else:
                manage=Manage.objects.get(id=key)
                form=Manage_form(request.POST,instance=manage)           


            form.save()
            form=Manage_form()


        if'delete' in request.POST:
            key=request.POST.get('delete')
            manage=Manage.objects.get(id=key)
            manage.delete()


        if'edit' in request.POST:
            key=request.POST.get('edit')
            manage=Manage.objects.get(id=key)
            form=Manage_form(instance=manage)
      




    manage=Manage.objects.all()
    context['manage']=manage
    context['form']=form
    return render(request,'index.html',context)