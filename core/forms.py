from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput, DateInput, DateTimeInput, TimeInput, CheckboxInput, Select
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "startDate"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del Proyecto"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'cols': 80, 'rows': 20}),
            'startDate': DateInput(attrs={'class': 'form-control'})
        }
