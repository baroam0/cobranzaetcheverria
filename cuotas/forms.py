
from django import forms
from expedientes.models import Expediente
from .models import Cuota



class CuotaForm(forms.ModelForm):
    expediente = forms.ModelChoiceField(
        queryset=Expediente.objects.all(), 
        label="Expediente", 
        required=True
    )

    descripcion = forms.CharField(label="Descripcion", required=False)

    importe = forms.DecimalField(label="Importe", required=True)

    def __init__(self, *args, **kwargs):
        super(CuotaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Cuota
        fields = ['expediente', 'descripcion', 'importe']
