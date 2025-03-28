
from django import forms
from expedientes.models import Expediente
from .models import Cuota


class CuotaForm(forms.ModelForm):
    
    fecha = forms.DateField(label="Fecha", required=True)

    expediente = forms.ModelChoiceField(
        queryset=Expediente.objects.all().order_by("expediente"), 
        label="Expediente", 
        required=True
    )

    descripcion = forms.CharField(label="Descripcion", required=False)

    importe = forms.DecimalField(label="Importe", required=True)
    importecomision = forms.DecimalField(label="Importe Comisión", required=False)

    def __init__(self, *args, **kwargs):
        super(CuotaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Cuota
        fields = ['fecha', 'expediente', 'descripcion', 'importe', 'importecomision']
