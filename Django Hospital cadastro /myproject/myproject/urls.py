from django.urls import path
from megaapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pacienteInfo',views.hospital,name='paciente_usuario')
]
