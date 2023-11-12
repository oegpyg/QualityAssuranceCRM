from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput, DateInput, DateTimeInput, TimeInput, CheckboxInput, Select
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "startDate", "reporter", "status", "priority", "productOwner", "developer", "qa", "stakeHolder", "assignedTo", "version", "businessUnit", "typeOfTests"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del Proyecto"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'cols': 80, 'rows': 20}),
            'startDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de Inicio"}),
            'reporter': TextInput(attrs={'class': 'form-control', 'placeholder': "Reportado por"}),
            'status': TextInput(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            'priority': TextInput(attrs={'class': 'form-control', 'placeholder': "Prioridad"}),
            'productOwner': TextInput(attrs={'class': 'form-control', 'placeholder': "Dueño del Producto"}),
            'developer': TextInput(attrs={'class': 'form-control', 'placeholder': "Desarrollador"}),
            'qa': TextInput(attrs={'class': 'form-control', 'placeholder': "Tester de Calidad"}),
            'stakeHolder': TextInput(attrs={'class': 'form-control', 'placeholder': "StakeHolder"}),
            'assignedTo': TextInput(attrs={'class': 'form-control', 'placeholder': "Asignado a"}),
            'version': TextInput(attrs={'class': 'form-control', 'placeholder': "Version"}),
            'businessUnit': TextInput(attrs={'class': 'form-control', 'placeholder': "Unidad de negocio"}),
            'typeOfTests': TextInput(attrs={'class': 'form-control', 'placeholder': "Tipo de Pruebas"}),
        }

        class ProjectForm(ModelForm):
    class Meta:
        model = Release
        fields = ["title", "description", "project", "status", "reporter", "assignedTo", "priority", "version", "typeOfTests", "qaDeploymentPlanningDate", "testPlanCreationDate", "testStartDate", "testEndDate", "plannedImplementationDate", "finalImplementationDate", "productOwner", "developer", "qa"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del Proyecto"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'cols': 80, 'rows': 20}),
            'project': TextInput(attrs={'class': 'form-control', 'placeholder': "Proyecto"}),
            'status': TextInput(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            'reporter': TextInput(attrs={'class': 'form-control', 'placeholder': "Reportado por"}),
            'assignedTo': TextInput(attrs={'class': 'form-control', 'placeholder': "Asignado a"}),
            'priority': TextInput(attrs={'class': 'form-control', 'placeholder': "Prioridad"}),
            'version': TextInput(attrs={'class': 'form-control', 'placeholder': "Version"}),
            'typeOfTests': TextInput(attrs={'class': 'form-control', 'placeholder': "Tipo de Pruebas"}),
            'qaDeploymentPlanningDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha planificada despliegue QA"}),
            'testPlanCreationDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de creación del plan de pruebas"}),
            'testStartDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de inicio de pruebas"}),
            'testEndDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de finalización de pruebas"}),
            'plannedImplementationDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha planificada de Implementación"}),
            'finalImplementationDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de implementación"}),
            'productOwner': TextInput(attrs={'class': 'form-control', 'placeholder': "Dueño del Producto"}),
            'developer': TextInput(attrs={'class': 'form-control', 'placeholder': "Desarrollador"}),
            'qa': TextInput(attrs={'class': 'form-control', 'placeholder': "Tester de Calidad"}),
        }
