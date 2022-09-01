
from django import forms
from .models import Cliente


class ExpedienteForm(forms.ModelForm):    
    expediente = forms.CharField(label="Expediente")
    descripcion = forms.CharField(label="Descripcion")
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all().order_by("apellido"), label="Cliente")
    monto = forms.DecimalField(label="Monto")
    

    def __init__(self, *args, **kwargs):
        super(ExpedienteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Cliente
        fields = ['expediente', 'descripcion', 'cliente',
            'monto']
