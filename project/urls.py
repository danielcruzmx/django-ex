from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from main import views

#from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-rest/olimpo/informe/(?P<depto_id>[\w]+)/$',
    views.CuotasViewSet.as_view(), name='my_rest_view'),
    url(r'^api-rest/totalIngresosEgresos/(?P<condominio>[\w]+)/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
    views.TotalIngresosEgresosViewSet.as_view(), name='my_rest_view'),
    url(r'^api-rest/cuotasDeptoMes/(?P<condominio>[\w]+)/(?P<mes_anio>(0?[1-9]|1[012])-((19|20)\d\d))/$',
    views.CuotasDeptoMesViewSet.as_view(), name='my_rest_view'),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^explorer/', include('explorer.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
