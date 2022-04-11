from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ChildSignUpForm, ParentSignUpForm
from .models import Task, ParentUser



# django auth


def login_view(request):
    # if POST, then authenticate the user (submitting the username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: # it was a get request so send the empty login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def parent_signup_view(request):
    # user_type = 'Parent'
    # registered= False
    if request.method == "POST":
       
        form = ParentSignUpForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            user.is_parent = True
            user.save()
            login(request, user)
            return HttpResponseRedirect('/login/')
        else:
            form = ParentSignUpForm()
            return render(request, 'parent_signup.html', {'form': form})
    else:
        form = ParentSignUpForm()
        return render(request,'parent_signup.html',{'form': form})

        

def child_signup_view(request):
#     # user_type = 'Child'
#     # registered= False
    if request.method == "POST":
       
        form = ChildSignUpForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            user.is_child = True
            user.save()
            login(request, user)
            return HttpResponseRedirect('/login/')
        else:
            form = ChildSignUpForm()
            return render(request, 'child_signup.html', {'form': form})
    else:
        form = ChildSignUpForm()
        return render(request,'child_signup.html',{'form': form})



# Create your views here.

class LandingPage(TemplateView): 
    template_name = 'landing_page.html'

class Dashboard(TemplateView): 
    template_name = 'dashboard.html'



class TaskList(TemplateView):
    template_name = 'tasklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context['tasks'] = Task.objects.filter(name_icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['tasks'] = Task.objects.all()
            context['header'] = "Daily Tasks" # this is where we add the key into our context object for the view to use
        return context 


# Tasks CRUD

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'amount', 'due_date', 'description', 'task_status', 'task_approval', 'user']
    template_name = "task_create.html"
    success_url = '/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/tasks')


class TaskDetail(DetailView): 
    model = Task
    template_name="task_detail.html"


class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'amount', 'due_date', 'description', 'task_status', 'task_approval', 'user']
    template_name = "task_update.html"
    # success_url = "/tasks/"
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDelete(DeleteView):
    model = Task
    template_name = "task_delete_confirmation.html"
    success_url = "/tasks/"


def profile(request, username):
    user = User.objects.get(username=username)
    tasks = Task.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'tasks': tasks})


# Families view function

# def familygroup_index(request):
#     familygroups = FamilyGroup.objects.all()
#     return render(request, 'familygroup_index.html', {'familygroups': familygroups})

# def familygroup_show(request, familygroup_id):
#     familygroup = FamilyGroup.objects.get(id=familygroup_id)
#     return render(request, 'familygroup_show.html', {'familygroup': familygroup})



# class FamilyGroupCreate(CreateView):
#     model = Task
#     fields = ['name', 'description']
#     template_name = "familygroup_create.html"
#     success_url = "/familygroups/"



# class FamilyGroupUpdate(UpdateView):
#     model = Task
#     fields = ['name', 'description']
#     template_name = "familygroup_update.html"
#     success_url = "/familygroups/"


# class FamilyGroupDelete(DeleteView):
#     model = Task
#     template_name = "familygroup_delete_confirmation.html"
#     success_url = "/familygroups/"



#Parent User CRUD
# class ParentDetail(DetailView): 
#     model = Task
#     template_name="parent_detail.html"


#ChildrenInFamily CRUD
# def childreninfamily_index(request):
#     childreninfamilys = ChildrenInFamily.objects.all()
#     return render(request, 'childreninfamily_index.html', {'childreninfamilys': childreninfamilys})

# def childreninfamily_show(request, childreninfamily_id):
#     childreninfamily = ChildrenInFamily.objects.get(id=childreninfamily_id)
#     return render(request, 'childreninfamily_show.html', {'childreninfamily': childreninfamily})



# class ChildrenInFamilyCreate(CreateView):
#     model = User
#     fields = ['parent', 'child']
#     template_name = "childreninfamily_create.html"
#     success_url = "/childreninfamily/"



# class ChildrenInFamilyUpdate(UpdateView):
#     model = User
#     fields = ['parent', 'child']
#     template_name = "childreninfamily_update.html"
#     success_url = "/childreninfamily/"


# class ChildrenInFamilyDelete(DeleteView):
#     model = User
#     template_name = "childreninfamily_delete_confirm.html"
#     success_url = "/childreninfamily/"