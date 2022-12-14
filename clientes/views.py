
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import ClienteForm
from .models import Cliente


def controladni(dni,pk):
    try:
        consulta = Cliente.objects.filter(numerodocumento=dni).exclude(pk=pk)
        return 1
    except:
        return 0    


def listadocliente(request):
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        consulta = Cliente.objects.filter(
            Q(apellido__icontains=parametro) |
            Q(nombre__contains=parametro)
        ).order_by('apellido')
    else:
        consulta = Cliente.objects.all().order_by('apellido')

    paginador = Paginator(consulta, 20)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    resultados = paginador.get_page(page)
    return render(request, 'clientes/cliente_list.html', {'resultados': resultados})


def nuevocliente(request):
    if request.POST:
        form = ClienteForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            consulta = Cliente.objects.latest('pk')
            messages.success(
                request,
                "SE HAN GUARDADO LOS DATOS DEL CLIENTE " + str(consulta.apellido).upper() + ', ' + str(consulta.nombre).upper())
            return redirect('/listadocliente/')
        else:
            return render(
                request,
                'clietnes/cliente_nuevo.html',
                {"form": form}
            )
    else:
        form = ClienteForm()
        return render(
            request,
            'clientes/cliente_nuevo.html',
            {
                "form": form,
            }
        )


def editarcliente(request, pk):
    consulta = Cliente.objects.get(pk=pk)

    if request.POST:
        form = ClienteForm(request.POST, instance=consulta)

        if form.is_valid():
            form.save()
            messages.success(request, "SE HA MOFICICADO EL CLIENTE")
            return redirect('/listadocliente')
        else:
            return render(request, "clientes/clientes_edit.html", {"form": form})
    else:
        form = ClienteForm(instance=consulta)

        return render(
            request,
            'clientes/cliente_nuevo.html',
            {
                "form": form,
            }
        )

# Create your views here.
