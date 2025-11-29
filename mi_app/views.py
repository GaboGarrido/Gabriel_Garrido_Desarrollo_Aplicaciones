from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Actividad
from .forms import ActividadForm


def lista_actividades(request):
    q = request.GET.get('q', '').strip()
    actividades = Actividad.objects.order_by('-fecha_creacion')
    if q:
        actividades = actividades.filter(
            Q(titulo__icontains=q) | Q(descripcion__icontains=q)
        )
    total = actividades.count()
    completadas = actividades.filter(completada=True).count()
    pendientes = total - completadas
    context = {
        'actividades': actividades,
        'total': total,
        'completadas': completadas,
        'pendientes': pendientes,
        'q': q,
    }
    return render(request, 'mi_app/lista_actividades.html', context)


def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ActividadForm()
    return render(request, 'mi_app/actividad_form.html', {'form': form, 'title': 'Crear Actividad'})


def editar_actividad(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'mi_app/actividad_form.html', {'form': form, 'title': 'Editar Actividad'})


def borrar_actividad(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        actividad.delete()
        return redirect('home')
    return render(request, 'mi_app/actividad_confirm_delete.html', {'actividad': actividad})


def toggle_actividad(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    actividad.completada = not actividad.completada
    actividad.save()
    return redirect('home')