
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import ExpedienteForm
from .models import Expediente


def listadoexpediente(request):
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        consulta = Expediente.objects.filter(
            Q(expediente__icontains=parametro) |
            Q(cliente__apellido__icontains=parametro) |
            Q(cliente__nombre__icontains=parametro)
        ).order_by('expediente')
    else:
        consulta = Expediente.objects.all().order_by('expediente')

    paginador = Paginator(consulta, 20)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    resultados = paginador.get_page(page)
    return render(request, 'expedientes/expediente_list.html', {'resultados': resultados})


def nuevoexpediente(request):
    if request.POST:
        form = ExpedienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "SE HAN GUARDADO LOS DATOS DEL EXPEDIENTE ")
            return redirect('/listadoexpediente/')
        else:
            return render(
                request,
                'expedientes/expediente_nuevo.html',
                {"form": form}
            )
    else:
        form = ExpedienteForm()
        return render(
            request,
            'expedientes/expediente_nuevo.html',
            {
                "form": form,
            }
        )


def editarexpediente(request, pk):
    consulta = Expediente.objects.get(pk=pk)

    if request.POST:
        form = ExpedienteForm(request.POST, instance=consulta)

        if form.is_valid():
            form.save()
            messages.success(request, "SE HA MOFICICADO EL EXPEDIENTE")
            return redirect('/listadoexpediente')
        else:
            return render(request, "expedientes/expedientes_nuevo.html", {"form": form})
    else:
        form = ExpedienteForm(instance=consulta)

        return render(
            request,
            'expedientes/expediente_nuevo.html',
            {
                "form": form,
            }
        )


# Create your views here.
