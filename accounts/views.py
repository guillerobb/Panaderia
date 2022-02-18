from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from accounts.forms import CreateUserForm
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required(login_url='/login/')
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Cuenta creada para el Usuario ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

class UserListView(generic.ListView):
    template_name = 'accounts/users_list.html'
    context_object_name = 'users_list'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return User.objects.all()

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'accounts/user_detail.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(generic.CreateView):
    model = User
    template_name = 'accounts/user_form.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'username',
        'is_active',
        ]
    success_url = '/accounts/'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserUpdateView(generic.UpdateView):
    model = User
    template_name = 'accounts/user_update.html'

    fields = [
        'first_name',
        'last_name',
        'email',
        'username',
        'is_active',
    ]

    success_url = '/accounts/'
    success_message = 'Usuario Actualizado.'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserDeleteView(generic.DeleteView):
    model = User
    success_url = '/accounts/'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def loginPage(request):
    print('======================= login =================================')
    context = {}
    print(request)
    print(request.method)
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print('username:', username)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print('is not None')
                login(request, user)
                #return redirect('index')
                return render(request, 'index.html')
            else:
                print('Usuario o Contraseña es incorrecta')
                messages.info(request, 'Usuario o Contraseña es incorrecta')
        
    
    return render(request, 'accounts/login.html', context)

@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request)
    return render(request, 'accounts/login.html')