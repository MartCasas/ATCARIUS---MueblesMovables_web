from django.urls import path
from .views import index ,mueblesmovablesproductos,agregarProducto,listarProductos,registro,eliminarProductos,modificarProductos,InicioSesion

urlpatterns = [
    path('',index, name='index'),
    path('mueblesmovablesproductos/',mueblesmovablesproductos,name='mueblesmovablesproductos'),
    path('agregarProducto/',agregarProducto, name="agregarProducto"),
    path('listarProductos/',listarProductos, name="listarProductos"),
    path('registro/',registro, name="registro"),
    path('eliminarProductos/<id>/',eliminarProductos, name="eliminarProductos"),
    path('modificarProductos/<id>/',modificarProductos, name="modificarProductos"),
        path('InicioSesion/',InicioSesion, name="InicioSesion"),

]
