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

class ReleaseForm(ModelForm):
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

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "typeTask", "associatedRealease", "status", "assignedTo", "description", "comments"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del Proyecto"}),
            'typeOfTask': TextInput(attrs={'class': 'form-control', 'placeholder': "Tipo de Tarea"}),
            'associatedRealease': TextInput(attrs={'class': 'form-control', 'placeholder': "Entrega relacionada"}),
            'status': TextInput(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            'assignedTo': TextInput(attrs={'class': 'form-control', 'placeholder': "Asignado a"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'cols': 80, 'rows': 20}),
            'comments': TextInput(attrs={'class': 'form-control', 'placeholder': "Comentarios"}),
            
        }

class QaDocumentationForm(ModelForm):
    class Meta:
        model = QaDocumentation
        fields = ["TestPlans", "productOwnerApproval", "status", "developerApproval", "evidenceOfTheTestPlans",]
        widgets = {
            'TestPlans': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del Plan de Pruebas"}),
            'productOwnerApproval': TextInput(attrs={'class': 'form-control', 'placeholder': "Aprobación del Dueño del producto"}),
            'status': TextInput(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            'developerApproval': TextInput(attrs={'class': 'form-control', 'placeholder': "Aprobación del Desarrollador"}),
            'evidenceOfTheTestPlans': Textarea(attrs={'class': 'form-control', 'placeholder': 'Evidencias del plan de pruebas'}),
        }

class ChecklistDocumentationForm(ModelForm):
    class Meta:
        model = ChecklistDocumentation
        fields = ["typeOfTests", "releasePlatformAffected", "status", "developerApproval", "evidenceOfTheTestPlans",]
        widgets = {
            'typeOfTests': TextInput(attrs={'class': 'form-control', 'placeholder': "Tipo de Pruebas"}),
            'releasePlatformAffected': TextInput(attrs={'class': 'form-control', 'placeholder': "Entrega relacionada"}),
            'qaDocumentation': TextInput(attrs={'class': 'form-control', 'placeholder': "Documentación QA"}),
        }

class ReportedBugsForm(ModelForm):
    class Meta:
        model = ReportedBugs
        fields = ["title", "typeInput", "reporter", "assignedTo", "",]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Título del error"}),
            'typeInput': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción del Error"}),
            'reporter': TextInput(attrs={'class': 'form-control', 'placeholder': "Reportado por"}),
            'assignedTo': TextInput(attrs={'class': 'form-control', 'placeholder': "Asignado a"}),
        }

class ImplementationReleaseForm(ModelForm):
    class Meta:
        model = ImplementationRelease
        fields = ["description", "idRelease", "ImplementationDate", "Documentation", "developerInCharge","qaInCharge","results","descriptionResult","testEvidence"]
        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción"}),
            'idRelease': TextInput(attrs={'class': 'form-control', 'placeholder': "Entrega relacionada"}),
            'Documentation': DateInput(attrs={'class': 'form-control', 'placeholder': "Documentación"}),
            'developerInCharge': TextInput(attrs={'class': 'form-control', 'placeholder': "Desarrollador a cargo"}),
            'qaInCharge': TextInput(attrs={'class': 'form-control', 'placeholder': "Tester a cargo"}),
            'results': TextChoices(attrs={'class': 'form-control', 'placeholder': ("Exitoso", "Fallido")}),
            'descriptionResult': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción de resultados"}),
            'testEvidence': TextInput(attrs={'class': 'form-control', 'placeholder': "Evidencias de las pruebas"}),
        }

class TestEjecutionForm(ModelForm):
    class Meta:
        model = TestEjecution
        fields = ["id", "title", "generalDescription", "implementationRelease"]
        widgets = {
            'id': TextInput(attrs={'class': 'form-control', 'placeholder': "Identificador"}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Título"}),
            'generalDescription': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción general"}),
            'implementationRelease': TextInput(attrs={'class': 'form-control', 'placeholder': "Entrega relacionada"}),
        }


class CaseTestForm(ModelForm):
    class Meta:
        model = CaseTest
        fields = ["id", "title","caseTestDescription", "caseTestPreconditions", "caseOrder", "caseSteps", "caseExpectedOutcome", "testEjecution"]
        widgets = {
            'id': TextInput(attrs={'class': 'form-control', 'placeholder': "Identificador"}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Título"}),
            'caseTestDescription': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción"}),
            'caseTestPreconditions': TextInput(attrs={'class': 'form-control', 'placeholder': "Precondiciones"}),
            'caseOrder': TextInput(attrs={'class': 'form-control', 'placeholder': "Orden del caso de prueba"}),
            'caseSteps': TextInput(attrs={'class': 'form-control', 'placeholder': "Pasos a Seguir"}),
            'caseExpectedOutcome': TextInput(attrs={'class': 'form-control', 'placeholder': "Resultado Esperado"}),
            'testEjecution': TextInput(attrs={'class': 'form-control', 'placeholder': "Plan de pruebas relacionado"}),
        }

class QaDocumentationCaseTestImpForm(ModelForm):
    class Meta:
        model = QaDocumentationCaseTestImp
        fields = ["id", "caseTest","qaDocumentation"]
        widgets = {
            'id': TextInput(attrs={'class': 'form-control', 'placeholder': "Identificador"}),
            'caseTest': TextInput(attrs={'class': 'form-control', 'placeholder': "Caso de prueba"}),
            'qaDocumentation': TextInput(attrs={'class': 'form-control', 'placeholder': "Documentación QA"}),
        }









