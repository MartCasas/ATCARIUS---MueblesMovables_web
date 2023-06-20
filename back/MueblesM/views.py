from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from .forms import ProductoForm,Mueble, CustomUserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):

    return render(request, 'MueblesM/index.html')

def InicioSesion(request):

     return render(request,'MueblesM/InicioSesion.html')


# def RegistroSesion(request):

#     return render(request,'MueblesM/RegistroSesion.html')



def mueblesmovablesproductos(request):

    return render(request,'MueblesM/mueblesmovablesproductos.html')


# def login(request):

#     return render(request,'MueblesM/registration/login.html')



def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method  == 'POST':
        formulario = CustomUserCreationForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success (request, "te has registrado correctamente")
            #redirigir al index
            return redirect(to='index')
        data["form"] = formulario
    return render(request ,'MueblesM/registration/registro.html',data)


def agregarProducto(request):

    data = {
        'form': ProductoForm()

    }
    if request.method ==  'POST':
        formulario = ProductoForm(data=request.POST, files=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'MueblesM/muebles/agregar.html',data)


def listarProductos(request):

    productos = Mueble.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'MueblesM/muebles/listar.html',data)


def modificarProductos(request, id):

    producto = get_object_or_404(Mueble, id=id)

    data = {
        'form': ProductoForm(instance=producto),
    }
    if request.method ==  'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "modificado correctamente"
            return redirect(to="listarProductos")
        else:
            data["form"] = formulario
    return render(request ,'MueblesM/muebles/modificar.html',data)


def eliminarProductos(request, id):
    producto = get_object_or_404(Mueble, id=id)
    producto.delete()
    return redirect(to="listarProductos")
