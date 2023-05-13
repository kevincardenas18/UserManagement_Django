from django.contrib import admin
from .models import Cliente
from .models import Mesa
from .models import Reserva
from .models import Categoria
from .models import Menu
from .models import Pedido
from .models import Factura

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mesa)
admin.site.register(Reserva)
admin.site.register(Categoria)
admin.site.register(Menu)
admin.site.register(Pedido)
admin.site.register(Factura)