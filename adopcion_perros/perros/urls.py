from django.urls import path
from . import views

urlpatterns = [
    path('registro_perro/', views.registro_perro, name='registro_perro'),
    path('recomendaciones/<int:usuario_id>/', views.recomendaciones, name='recomendaciones'),
]
