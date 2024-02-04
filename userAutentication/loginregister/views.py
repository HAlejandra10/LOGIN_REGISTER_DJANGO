from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
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

