from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    #user is sending the form through Post method
    if request.method == 'POST':
        formulario = LoginForm(request.POST) 
        if formulario.is_valid():
            cd = formulario.cleaned_data
            user = authenticate(request,
                                username = cd["username"],
                                password = cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("El usuario está autenticado")
            else: 
                    return HttpResponse("El usuario no está activo")
        else:
                HttpResponse("La informacion no es correcta")
    else:
        formulario = LoginForm()
        return render(request, "cuenta/login.html" ,{"form":formulario}) #18:51

@login_required
def dashboard(request):
    return render(request, "cuenta/dashboard.html")


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
            return render(request,'account/register.html',
                          {'user_form': user_form})
            
            