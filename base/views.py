from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from.forms import RegistrationForm,CreateTask,UpdateTask
from django.contrib.auth import login
from .models import Tasks

# Create your views here.




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(reverse_lazy('home'))
            

    else:
        form = RegistrationForm()
        args = {'form':form}

        return render(request,'base/register.html',args)


class CustomizeLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def createtask(request):

    if request.method=='POST':
        form = CreateTask(request.POST)
        form.instance.user = request.user

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        
    else:
        form = CreateTask()
        args ={'form':form}

        return render(request,'base/createtask.html',args)
    

def home(request):

    args ={}
 
    
    args["tasks"] = Tasks.objects.filter(user=request.user.id)
    args['count']= args['tasks'].filter(complete=False).count()

    search_input = request.GET.get('search-area') or ''

    if search_input:
        args["tasks"]= args["tasks"].filter(title__startswith=search_input)

    args['search_input']= search_input
         
    return render(request, "base/home.html", args)


def updatetask(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method=='POST':
        form = UpdateTask(request.POST,instance=task)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        
    else:
        form = UpdateTask()
        args ={'form':form}

        return render(request,'base/updatetask.html',args)


def deletetask(request,pk):
    task =  get_object_or_404(Tasks,pk=pk)
    if request.method=='POST':
        task.delete()
        return redirect(reverse_lazy('home'))
    else:
        args = {'task':task}
        return render(request,'base/confirmdelete.html',args)


def taskdetails(request,pk):
    task = get_object_or_404(Tasks,pk=pk)

    args ={'task':task}

    return render(request,'base/taskdetail.html',args)