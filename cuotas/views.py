
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

    form = CuotaForm()

    saldo = expediente.monto - importecuotas

    return render(
        request, 
        'cuotas/cuota_list.html',
        {
            'form': form,
            'expediente' : expediente,
            'importecuotas' : importecuotas,
            'resultados': cuotas,
            'saldo': saldo
        }
    )


def nuevocuota(request):
    if request.POST:
        form = CuotaForm(request.POST)

        print("**********************")
        print(form['expediente'].value())

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

# Create your views here.
