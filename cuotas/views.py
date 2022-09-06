
from django.contrib import messages
from django.shortcuts import render, redirect

from expedientes.models import Expediente
from .forms import CuotaForm
from .models import Cuota


def listadocuota(request, pk):

    expediente = Expediente.objects.get(pk=pk)
    cuotas = Cuota.objects.filter(expediente=expediente.pk).order_by('fecha')

    importecuotas = 0
    for i in cuotas:
        importecuotas = importecuotas + i.importe
    
    importecuotascomision = 0
    for i in cuotas:
        if i.importecomision:
            importecuotascomision = importecuotascomision + i.importecomision

    form = CuotaForm()

    saldo = expediente.monto - importecuotas - importecuotascomision

    return render(
        request, 
        'cuotas/cuota_list.html',
        {
            'form': form,
            'expediente' : expediente,
            'importecuotas' : importecuotas,
            'importecuotascomision' : importecuotascomision,
            'resultados': cuotas,
            'saldo': saldo
        }
    )


def nuevocuota(request):
    if request.POST:
        form = CuotaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "SE HAN GUARDADO LOS DATOS")
            return redirect('/listadocuota/' + str(form['expediente'].value()))
        else:
            return render(
                request,
                'cuotas/cuota_list.html',
                {"form": form}
            )
    """
    else:
        form = CuotaForm()
        return render(
            request,
            'cuotas/cuota_nuevo.html',
            {
                "form": form,
            }
        )
    """


def reporte(request):
    
    if "txtMes" in request.GET and "txtAnio" in request.GET:
        parametromes = request.GET.get("txtMes")
        parametroanio = request.GET.get("txtAnio")

        resultados = Cuota.objects.filter(
            fecha__year__gte=parametroanio,
            fecha__month__gte=parametromes,
            fecha__year__lte=parametroanio,
            fecha__month__lte=parametromes
        )
        return render(request, 'cuotas/reporte.html', {'resultados': resultados})
    else:
        return render(request, 'cuotas/reporte.html')
    

# Create your views here.
