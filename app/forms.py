from django.forms import ModelForm
from .models import Modelo

class ModeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = ['nome','sobrenome']