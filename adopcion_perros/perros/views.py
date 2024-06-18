from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Perro, Usuario
from .utils import analizar_descripcion


def registro_perro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        imagen = request.FILES['imagen']
        perro = Perro.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            imagen=imagen
        )
        return JsonResponse({'mensaje': 'Perro registrado exitosamente!'})
    return render(request, 'registro_perro.html')

def recomendaciones(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    preferencias = analizar_descripcion(usuario.preferencias)
    perros = Perro.objects.all()  # Aquí se podría mejorar con un filtrado basado en las preferencias
    return render(request, 'recomendaciones.html', {'perros': perros})
