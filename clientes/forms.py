
from django import forms
from django.contrib.auth.models import User

from .models import TipoDocumento, Paciente
from apps.catalogosenfermedades.models import Catalogo
from apps.obrassociales.models import ObraSocial
from apps.pacientes.models import Paciente, PacienteObraSocial
from apps.profesionales.models import Profesional


class ClienteForm(forms.ModelForm):    
    apellido = forms.CharField(label="Apellido", required=True)
    nombre = forms.CharField(label="Nombre", required=True)
    numerodocumento = forms.CharField(label="Numero Documento", required=False)
    telefono = forms.CharField(label="Telefono", required=False)
    domicilio = forms.CharField(label="Domicilio", required=False)
    profesion = forms.CharField(label="Ocupacion", required=False)


    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'nombre', 'numero_documento',
            'fecha_nacimiento', 'telefono', 'telefono_opcional',
            'correo_electronico', 'domicilio', 'ocupacion', 'fecha_admision',
            'profesional_tratante', 'medicacion', 'fue_al_psicologo',
            'grupo_familiar', 'diagnostico', 'observacion']


class PacienteObraSocialForm(forms.ModelForm):
    """
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(), 
        label="Paciente",
        required=True
    )
    """
    obrasocial = forms.ModelChoiceField(
        queryset=ObraSocial.objects.all().order_by("descripcion"), 
        label="Obra Social",
        required=True
    )
    numeroafiliado = forms.CharField(
        label="Numero Afiliado", required=False)

    observaciones = forms.CharField(
        widget=forms.Textarea, label="Observaciones", required=False)

    def __init__(self, *args, **kwargs):
        super(PacienteObraSocialForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'width:100%'
            })

    class Meta:
        model = PacienteObraSocial
        fields = ['obrasocial', 'numeroafiliado', 'observaciones']

