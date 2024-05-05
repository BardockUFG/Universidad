from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('registrarRutas/', views.registrarRutas),
    path('edicionRuta/<codigo>',views.edicionRuta),
    path('editarRutas/', views.editarRutas),
    path('eliminacionRuta/<codigo>', views.eliminacionRuta)
]