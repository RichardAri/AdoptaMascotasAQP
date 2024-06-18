from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Perro, Usuario
from .forms import PerroForm
from .nlp_model import obtener_recomendaciones  # Suponiendo que tengas un módulo para el modelo NLP

def index(request):
    if request.method == 'POST':
        form = PerroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PerroForm()
    return render(request, 'perros/index.html', {'form': form})

def resultados(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        # Llama a tu función de procesamiento NLP aquí
        perros_recomendados = obtener_recomendaciones(descripcion)
        return render(request, 'perros/resultados.html', {'perros': perros_recomendados})
    else:
        return redirect('index')
