

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import ClienteForm
from .models import Cliente


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

"""
def ajax_obrasocial_paciente(request, pk):
    paciente  = Paciente.objects.get(pk=pk)

    pacientes_obrasociales = PacienteObraSocial.objects.filter(
        paciente=paciente
    )

    dict_tmp = dict()
    list_tmp = list()

    if pacientes_obrasociales:
        for dato in pacientes_obrasociales:
            dict_tmp["id_obrasocial"] = dato.obrasocial.pk
            dict_tmp["descripcion_obrasocial"] = dato.obrasocial.descripcion.upper()
            dict_tmp["abreviatura_obrasocial"] = dato.obrasocial.abreviatura.upper()
            list_tmp.append(dict_tmp)
            dict_tmp = dict()
    else:
        pacientes_obrasociales = None

    return JsonResponse(list_tmp, safe=False)


def ajax_profesionaltratante_paciente(request, pk):
    paciente  = Paciente.objects.get(pk=pk)
    profesional = Profesional.objects.get(pk=paciente.profesional_tratante.pk)
    nombre_profesional = str(profesional.usuario.first_name) + ', ' + str(profesional.usuario.last_name)

    dict_tmp = dict()
    list_tmp = list()

    if paciente:
        dict_tmp["id_profesional"] = profesional.pk
        dict_tmp["profesional"] = nombre_profesional.upper()
        list_tmp.append(dict_tmp)
    else:
        paciente = None

    return JsonResponse(list_tmp, safe=False)


@csrf_exempt
def ajax_nuevopacienteobrasocial(request):
    datos = ast.literal_eval(request.POST["datos"]) 
    paciente = Paciente.objects.get(pk=datos["paciente"])
    obraosocial = ObraSocial.objects.get(pk=int(datos["obrasocial"]))
    paciente_obrasocial = PacienteObraSocial(
        paciente = paciente,
        obrasocial = obraosocial,
        numeroafiliado = datos["numeroafiliado"],
        observaciones = datos["observaciones"],
    )
    paciente_obrasocial.save()
    
    consulta = PacienteObraSocial.objects.filter(paciente=paciente)

    dict_tmp = dict()
    list_tmp = list()

    if len(consulta) > 0:
        for i in consulta:
            dict_tmp["id_pacienteobrasocial"] = i.pk
            dict_tmp["id_obrasocial"] = i.obrasocial.pk
            dict_tmp["descripcion"] = i.obrasocial.descripcion.upper()
            dict_tmp["numeroafiliado"] = i.numeroafiliado
            dict_tmp["observaciones"] = i.observaciones
            list_tmp.append(dict_tmp)
            dict_tmp = dict()

    return JsonResponse(list_tmp, safe=False)


@csrf_exempt
def ajax_editarpacienteobrasocial(request):
    datos = ast.literal_eval(request.POST["datos"])

    paciente_obrasocial = PacienteObraSocial.objects.get(pk=datos["paciente_obrasocial"])
    obraosocial = ObraSocial.objects.get(pk=int(datos["obrasocial"]))
  
    paciente_obrasocial.obrasocial=obraosocial
    paciente_obrasocial.numeroafiliado=datos["numeroafiliado"]
    paciente_obrasocial.observaciones=datos["observaciones"]

    paciente_obrasocial.save()

    paciente = Paciente.objects.get(pk=datos["paciente"])

    paciente_obrasocial = PacienteObraSocial.objects.filter(paciente=paciente)

    dict_tmp = dict()
    list_tmp = list()

    if len(paciente_obrasocial) > 0:
        for i in paciente_obrasocial:
            dict_tmp["id_pacienteobrasocial"] = i.pk
            dict_tmp["id_obrasocial"] = i.obrasocial.pk
            dict_tmp["descripcion"] = i.obrasocial.descripcion.upper()
            dict_tmp["numeroafiliado"] = i.numeroafiliado
            dict_tmp["observaciones"] = i.observaciones
            list_tmp.append(dict_tmp)
            dict_tmp = dict()

    return JsonResponse(list_tmp, safe=False)


def reportelistado(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(username=str(request.user.username))
        if not usuario.is_staff:
            usuarioprofesional = Profesional.objects.get(usuario=usuario)

    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")        
        if usuario.is_staff:
            consulta = Paciente.objects.filter(
                Q(apellido__icontains=parametro) |
                Q(nombre__contains=parametro)
            ).order_by('apellido')
        else:
            consulta = Paciente.objects.filter(
                Q(apellido__icontains=parametro) |
                Q(nombre__contains=parametro)
            ).filter(profesional_tratante=usuarioprofesional).order_by('apellido')
            #consulta = consulta.filter(profesional_tratante=usuarioprofesional)            
    else:
        if usuario.is_staff:
            consulta = Paciente.objects.all().order_by('apellido')
        else:
            consulta = Paciente.objects.filter(profesional_tratante=usuarioprofesional).order_by('apellido')

    paginador = Paginator(consulta, 20)
    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(request, 'pacientes/reporte_listado.html', {'resultados': resultados})

"""


# Create your views here.
