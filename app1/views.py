from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .models import Perfil, Password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseBadRequest
from django.contrib import messages
import random
import re


# Create your views here.


def index(request):
    return render(request, 'index.html')


def generator(request):
    return render(request, 'generator.html')

# vista para generar la contraseña


def passgen(request):
    lenght = int(request.GET.get('lenght'))
    character = list('abcdefghijklmnñopqrstwxyz')
    password_generated = ''

    if request.GET.get('uppercase'):
        character.extend(list('ABCDFGHIJKLMNÑOPQRSTWXYZ'))

    if request.GET.get('special'):
        character.extend(list('(-!#$%&()*,./:;?@[]^_`{|}~+<=>)'))

    if request.GET.get('number'):
        character.extend(list('0123456789'))

    for i in range(lenght):
        password_generated += random.choice(character)

    return render(request, 'generator.html', {'password': password_generated})


def register(request):
    return render(request, 'register.html')

# vista que maneja el registro de nuevo usuario


def signup(request):
    expresiones = {
        'usuario': r'^[a-zA-Z0-9\_\-]{4,16}$',
        'nombre': r'^[a-zA-ZÀ-ÿ\s]{1,30}$',
        'apellido': r'^[a-zA-ZÀ-ÿ\s]{1,50}$',
        'password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{4,12}$',
        'confirm_password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{4,12}$',
        'correo': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    }

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if not re.match(expresiones['usuario'], username):
            messages.error(request, 'Ingresa un nombre de usuario valido.')
            return redirect('signup')

        elif not re.match(expresiones['nombre'], firstname):
            messages.error(request, 'Ingresa un first name valido.')
            return redirect('signup')

        elif not re.match(expresiones['apellido'], lastname):
            messages.error(request, 'Ingresa un last name valido.')
            return redirect('signup')

        elif not re.match(expresiones['password'], password):
            messages.error(request, 'Ingresa una password valida.')
            return redirect('signup')

        elif not re.match(expresiones['correo'], email):
            messages.error(request, 'Ingresa un email valido.')
            return redirect('signup')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('signup')

        elif Perfil.objects.filter(email=email).exists():
            messages.error(request, 'Este email ya esta en uso.')
            return redirect('signup')

        elif password != confirm_password:
            messages.error(request, 'Las contraseñas deben ser iguales.')
            return redirect('signup')

        else:

            user = User.objects.create_user(
                username=username, password=password)

            perfil = Perfil(user=user, name=firstname,
                            lastname=lastname, email=email)
            perfil.save()

            return redirect(reverse('login') + '?ok')

    return render(request, 'register.html')

# vista de la pagina de perfil del usuario


@login_required
def profile(request):
    perfil = Perfil.objects.select_related('user').prefetch_related(
        'password_set').get(user=request.user)
    contraseñas = perfil.password_set.all()

    if request.method == 'POST':
        name_pass = request.POST['name_password']
        pass_add = request.POST['password_add']

        new_password_user = Password(
            user_pw=request.user.perfil, name_pw=name_pass, password=pass_add)
        new_password_user.save()

    return render(request, 'profile.html', {'perfil': perfil, 'contraseñas': contraseñas})


# vista para eliminar password de la lista de usuario
@login_required
def delete(request, id):
    pass_delete = Password.objects.get(id=id)
    pass_delete.delete()
    return redirect('profile')


# vista que devuelve la pagina para editar un registro de password con us id correspondiente
@login_required
def edit(request, id):
    pass_name = Password.objects.get(id=id)

    return render(request, 'edit.html', {'pass_name': pass_name})

# vista recibe el form para editar la password


@login_required
def editpass(request):
    if request.method == 'POST':
        id = request.POST['id']
        name_pass = request.POST['name_password']
        pass_word = request.POST['password_add']

        if name_pass and pass_word:
            new_password = Password.objects.get(id=id)
            new_password.name_pw = name_pass
            new_password.password = pass_word
            new_password.save()

        else:
            messages.error(request, 'Debes llenar el formulario')
            return redirect('edit', id=id)

    return redirect('profile')

# vista para agregar password generadas por la appweb.


@login_required
def add_pass(request):
    if request.method == 'POST':
        name_pw = request.POST['name_password']
        new_pass = request.POST['new_password']

        if name_pw and new_pass:
            if request.user.is_authenticated:
                user = Perfil.objects.get(user=request.user)

                add_password = Password(
                    user_pw=user, name_pw=name_pw, password=new_pass)
                add_password.save()

                return redirect('profile')

    return HttpResponseBadRequest('Error en la solicitud')

# agrega una password "x" a mi lista de passwords.


@login_required
def add_pass_profile(request):
    if request.method == 'POST':
        name_pw = request.POST['name_password']
        new_pass = request.POST['new_password']

        if name_pw and new_pass:
            if request.user.is_authenticated:
                user = Perfil.objects.get(user=request.user)

                add_password = Password(
                    user_pw=user, name_pw=name_pw, password=new_pass)
                add_password.save()

                return redirect('profile')
    else:
        messages.error(request, 'Ingresa un nombre de usuario valido.')
        return redirect('/')

    return HttpResponseBadRequest('Error en la solicitud')
