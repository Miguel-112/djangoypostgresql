from django.contrib import admin



from gestionPedidos.models import Clientes,Articulos,Pedido

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):#en esta funcion colocamos que solo nos muestre esos 3 campos en el panel de admin
    list_display =("nombre","direccion","tfno")
    search_fields=("nombre","tfno") #aqui nos pone en el panel de administracion la busqueda por nombre y telefono

class ArticulosAdmin(admin.ModelAdmin):#aqui creamos un filtro por seccion en articulos
    list_filter=("seccion",)


class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")#nos muestra los campos que queremos en el panel de administracion
    list_filter=("fecha",)#filtramos por fechas
    date_hierarchy=("fecha")#nos crea un menu horiontal vemos en que fecha tenemos cada pedidos

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedido,PedidosAdmin)





