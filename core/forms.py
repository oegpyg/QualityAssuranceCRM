from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput, DateInput, DateTimeInput, TimeInput, CheckboxInput, Select, SelectDateWidget, ModelChoiceField
from .models import Project, Release, Task, QaDocumentation, ReportedBugs, ChecklistDocumentation, ImplementationRelease, TestEjecution, CaseTest, QaDocumentationCaseTestImp, _priorityChoices, TypeOfTests
from django.contrib.auth.models import User
from decouple import config

from tinymce.widgets import TinyMCE

devGroup = config('DEVGROUP')
pownerGroup = config('POWNERGROUP')


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ["title", "description", "startDate", "reporter", "status", "priority", "productOwner",
                  "developer", "qa", "stakeHolder", "assignedTo", "version", "businessUnit", "typeOfTests"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Proyecto'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'cols': 80, 'rows': 20}),
            'startDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de Inicio", "type": "date"}),
            # 'reporter': ModelChoiceField(queryset=User.objects.filter(groups__name=pownerGroup), widget=Select, empty_label="(Nothing)"),
            'status': Select(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            'priority': Select(choices=_priorityChoices, attrs={'class': 'form-control', 'placeholder': "Prioridad"}),

            'productOwner': Select(choices=[(choice.pk, choice) for choice in User.objects.filter(groups__name=pownerGroup)], attrs={'class': 'form-control', 'placeholder': "Dueño del Producto"}),
            'developer': Select(attrs={'class': 'form-control', 'placeholder': "Desarrollador"}),
            'qa': Select(attrs={'class': 'form-control', 'placeholder': "Tester de Calidad"}),
            'stakeHolder': Select(attrs={'class': 'form-control', 'placeholder': "StakeHolder"}),
            'assignedTo': Select(attrs={'class': 'form-control', 'placeholder': 'Asignado a'}),
            'version': NumberInput(attrs={'class': 'form-control', 'placeholder': "Version"}),
            'businessUnit': Select(attrs={'class': 'form-control', 'placeholder': "Unidad de negocio"}),
            'typeOfTests': Select(attrs={'class': 'form-control', 'placeholder': 'Tipo de Pruebas'}),
        }


class ReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = ["title", "description", "project", "status", "reporter", "assignedTo", "priority", "version", "typeOfTests", "qaDeploymentPlanningDate",
                  "testPlanCreationDate", "testStartDate", "testEndDate", "plannedImplementationDate", "finalImplementationDate", "productOwner", "developer", "qa"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del Release"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'cols': 80, 'rows': 20}),
            'project': Select(attrs={'class': 'form-control', 'placeholder': "Proyecto"}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            # 'reporter': TextInput(attrs={'class': 'form-control', 'placeholder': "Reportado por"}),
            'assignedTo': Select(attrs={'class': 'form-control', 'placeholder': 'Asignado a'}),
            'priority': Select(attrs={'class': 'form-control', 'placeholder': "Prioridad"}),
            'version': NumberInput(attrs={'class': 'form-control', 'placeholder': "Version"}),
            'typeOfTests': Select(attrs={'class': 'form-control', 'placeholder': "Tipo de Pruebas"}),
            'qaDeploymentPlanningDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha planificada despliegue QA", "type": "date"}),
            'testPlanCreationDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de creación del plan de pruebas", "type": "date"}),
            'testStartDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de inicio de pruebas", "type": "date"}),
            'testEndDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de finalización de pruebas", "type": "date"}),
            'plannedImplementationDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha planificada de Implementación", "type": "date"}),
            'finalImplementationDate': DateInput(attrs={'class': 'form-control', 'placeholder': "Fecha de implementación", "type": "date"}),
            'productOwner': Select(attrs={'class': 'form-control', 'placeholder': "Dueño del Producto"}),
            'developer': Select(attrs={'class': 'form-control', 'placeholder': "Desarrollador"}),
            'qa': Select(attrs={'class': 'form-control', 'placeholder': "Tester de Calidad"}),
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "typeTask", "associatedRealease",
                  "status", "assignedTo", "description", "comments"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre de la Tarea"}),
            'typeTask': Select(attrs={'class': 'form-control', 'placeholder': "Tipo de Tarea"}),
            'associatedRealease': Select(attrs={'class': 'form-control', 'placeholder': 'Entrega relacionada'}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            'assignedTo': Select(attrs={'class': 'form-control', 'placeholder': "Asignado a"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'cols': 80, 'rows': 20}),
            'comments': Textarea(attrs={'class': 'form-control', 'placeholder': "Comentarios"}),

        }


class QaDocumentationForm(ModelForm):
    class Meta:
        model = QaDocumentation
        fields = ["TestPlans", "productOwnerApproval", "status",
                  "developerApproval", "evidenceOfTheTestPlans",]
        widgets = {
            'TestPlans': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre del Plan de Pruebas"}),
            'productOwnerApproval': TextInput(attrs={'class': 'form-control', 'placeholder': "Aprobación del Dueño del producto"}),
            # 'status': TextInput(attrs={'class': 'form-control', 'placeholder': "Estado"}),
            # 'developerApproval': TextInput(attrs={'class': 'form-control', 'placeholder': "Aprobación del Desarrollador"}),
            # 'evidenceOfTheTestPlans': Textarea(attrs={'class': 'form-control', 'placeholder': 'Evidencias del plan de pruebas'}),
        }


class ChecklistDocumentationForm(ModelForm):
    class Meta:
        model = ChecklistDocumentation
        fields = ["typeOfTests", "releasePlatformAffected",
                  # "status", "developerApproval", "evidenceOfTheTestPlans",
                  ]
        widgets = {
            'typeOfTests': TextInput(attrs={'class': 'form-control', 'placeholder': "Tipo de Pruebas"}),
            'releasePlatformAffected': TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrega relacionada'}),
            'qaDocumentation': TextInput(attrs={'class': 'form-control', 'placeholder': "Documentación QA"}),
        }


class ReportedBugsForm(ModelForm):
    class Meta:
        model = ReportedBugs
        fields = ["title", "typeInput", "reporter", "assignedTo"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Título del error"}),
            'typeInput': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción del Error"}),
            'reporter': TextInput(attrs={'class': 'form-control', 'placeholder': "Reportado por"}),
            'assignedTo': TextInput(attrs={'class': 'form-control', 'placeholder': "Asignado a"}),
            'statusBugs_choices': Select(attrs={'class': 'form-control', 'placeholder': "Estado del Reporte"}, choices=(('New', 'Nuevo'),
                                                                                                                        ('MoreData',
                                                                                                                         'Es necesaria más información'),
                                                                                                                        ('Assig', 'Asignado'),
                                                                                                                        ('Resolv', 'Resuelto'),
                                                                                                                        ('Close', 'Cerrado'))),
            'category_choices': Select(attrs={'class': 'form-control', 'placeholder': "Categoría"}, choices=(('NoDisp', 'Funcionalidad no disponible'),
                                                                                                             ('Handling', 'Manejo de errores definidos'),
                                                                                                             ('IncImp', 'Implementación incorrecta'),
                                                                                                             ('improve', 'Mejora'),
                                                                                                             ('Secure', 'Error de Seguridad'),
                                                                                                             ('UserInt', 'Interfaz de usuario'),
                                                                                                             ('Usab', 'Usabilidad'),
                                                                                                             ('Navi', 'Navigabilidad'))),
            'priority_choices': Select(attrs={'class': 'form-control', 'placeholder': "Prioridad"}, choices=(('Block', 'Bloqueado'),
                                                                                                             ('Urg', 'Urgente'),
                                                                                                             ('High', 'Alto'),
                                                                                                             ('Ave', 'Medio'),
                                                                                                             ('Low', 'Bajo'))),
            'severity_choices': Select(attrs={'class': 'form-control', 'placeholder': "Severidad"}, choices=(('Cri', 'Crítico'),
                                                                                                             ('Ma', 'Mayor'),
                                                                                                             ('Mi', 'Menor'),
                                                                                                             ('Sug', 'Sugerencia'))),
            'frenquency_choices': Select(attrs={'class': 'form-control', 'placeholder': "Frecuencia"}, choices=(('Alw', 'Siempre'),
                                                                                                                ('Som', 'A veces'),
                                                                                                                ('Rand', 'Aleatorio'),
                                                                                                                ('NotTri', 'No se ha intentado'),
                                                                                                                ('NotRep', 'No reproducible'),
                                                                                                                ('Unknown', 'Desconocido')))
        }


class ImplementationReleaseForm(ModelForm):
    class Meta:
        model = ImplementationRelease
        fields = ["description", "idRelease", "ImplementationDate", "Documentation",
                  "developerInCharge", "qaInCharge",
                  # "results", "descriptionResult",
                  "testEvidence"]
        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción"}),
            'idRelease': TextInput(attrs={'class': 'form-control', 'placeholder': "Entrega relacionada"}),
            'Documentation': DateInput(attrs={'class': 'form-control', 'placeholder': "Documentación"}),
            'developerInCharge': TextInput(attrs={'class': 'form-control', 'placeholder': "Desarrollador a cargo"}),
            'qaInCharge': TextInput(attrs={'class': 'form-control', 'placeholder': "Tester a cargo"}),
            # 'results': TextChoices(attrs={'class': 'form-control', 'placeholder': ("Exitoso", 'Fallido')}),
            'descriptionResult': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción de resultados"}),
            'testEvidence': TextInput(attrs={'class': 'form-control', 'placeholder': "Evidencias de las pruebas"}),
        }


class TestEjecutionForm(ModelForm):
    class Meta:
        model = TestEjecution
        fields = ["id", "title", "generalDescription",
                  "release", 'typeOfTests']
        widgets = {
            'id': TextInput(attrs={'class': 'form-control', 'placeholder': "Identificador"}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Título"}),
            'generalDescription': Textarea(attrs={'class': 'form-control', 'placeholder': "Descripción general"}),
            'release': Select(attrs={'class': 'form-control', 'placeholder': "Entrega relacionada"}),
            'typeOfTests': Select(attrs={'class': 'form-control', 'placeholder': "Tipo de Prueba"}),
        }


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CaseTestForm(ModelForm):
    class Meta:
        model = CaseTest
        fields = ["id", "title", "caseTestDescription", "caseTestPreconditions",
                  "caseOrder", "caseSteps", "caseExpectedOutcome", "testEjecution"]
        widgets = {
            'id': TextInput(attrs={'class': 'form-control', 'placeholder': "Identificador"}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "Título"}),
            'caseTestDescription': TextInput(attrs={'class': 'form-control', 'placeholder': "Descripción"}),
            'caseTestPreconditions': TextInput(attrs={'class': 'form-control', 'placeholder': "Precondiciones"}),
            'caseOrder': NumberInput(attrs={'class': 'form-control', 'placeholder': "Orden del caso de prueba"}),
            'caseSteps': Textarea(attrs={'class': 'form-control tinymce', 'placeholder': "Paso a paso"}),
            'caseExpectedOutcome': Textarea(attrs={'class': 'form-control', 'placeholder': "Resultado Esperado"}),
            'testEjecution': Select(attrs={'class': 'form-control', 'placeholder': "Plan de pruebas relacionado"}),
        }


class QaDocumentationCaseTestImpForm(ModelForm):
    class Meta:
        model = QaDocumentationCaseTestImp
        fields = ["id", "caseTest", "qaDocumentation"]
        widgets = {
            'id': TextInput(attrs={'class': 'form-control', 'placeholder': "Identificador"}),
            'caseTest': TextInput(attrs={'class': 'form-control', 'placeholder': "Caso de prueba"}),
            'qaDocumentation': TextInput(attrs={'class': 'form-control', 'placeholder': "Documentación QA"}),
            'impTC': Select(attrs={'class': 'form-control', 'placeholder': "Importancia casos de prueba"}, choices=(('BAJA', 'Baja'),
                                                                                                                    ('MED', 'Media'),
                                                                                                                    ('ALTA', 'Alta')
                                                                                                                    )),
        }


class TypeTestForm(ModelForm):
    class Meta:
        model = TypeOfTests
        fields = ["title"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de Caso de Prueba'}),
        }
