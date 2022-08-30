
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):    
    apellido = forms.CharField(label="Apellido", required=True)
    nombre = forms.CharField(label="Nombre", required=True)
    numerodocumento = forms.IntegerField(label="Numero Documento", required=False)
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
        model = Cliente
        fields = ['apellido', 'nombre', 'numerodocumento',
            'telefono', 'domicilio', 'profesion']
