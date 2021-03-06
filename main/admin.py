from django.contrib import admin

# Register your models here.

from main.models import TipoMovimiento, Situacion, CuentaContable, \
                        Banco, Condominio, Proveedore, \
                        Periodo, TipoDocumento

class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class SituacionAdmin(admin.ModelAdmin):
    list_display = ('situacion',)

class CuentaContableAdmin(admin.ModelAdmin):
    list_display = ('num_cuenta', 'descripcion')
    list_filter = ('num_cuenta',)

class BancoAdmin(admin.ModelAdmin):
    list_display = ('clave','descripcion')

class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProveedoreAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'rfc', 'domicilio')

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('condominio', 'fecha_inicial', 'fecha_final')


admin.site.register(TipoMovimiento, TipoMovimientoAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Situacion, SituacionAdmin)
admin.site.register(CuentaContable, CuentaContableAdmin)
admin.site.register(Banco, BancoAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Proveedore, ProveedoreAdmin)
admin.site.register(Periodo, PeriodoAdmin)

