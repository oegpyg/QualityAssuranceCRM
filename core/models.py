# from msilib import typemask
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from decouple import config
_title_max_length = 100
_priorityChoices = (('BAJ', 'BAJA'),
                    ('MED', 'MEDIA'),
                    ('ALT', 'ALTA'))
devGroup = config('DEVGROUP')
pownerGroup = config('POWNERGROUP')


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50, blank=False, null=False, verbose_name='Descripción')
    target_flow = models.CharField(max_length=50, blank=False, null=False, verbose_name="Objetivo Flujo")
    status = models.BooleanField(default=False, verbose_name="Activo")

    class Meta:
        verbose_name_plural = 'Estados'

    def __str__(self) -> str:
        return f"{self.id} | {self.label}"

    class Admin(admin.ModelAdmin):
        search_fields = ['label', 'target_flow']
        list_filter = ['target_flow']
        list_display = ['id', 'label', 'target_flow', 'status']


class StatusHistory(models.Model):
    """To manage changes history of any records"""
    id = models.AutoField(primary_key=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, verbose_name="Estado")
    record = models.CharField(max_length=20, verbose_name="Descripción")
    record_id = models.IntegerField(
        null=False, blank=False, verbose_name="Identificador de Descripción")
    transDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Usuario")

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name_plural = 'Historial de Estados'


class BusinessUnit(models.Model):
    id = models.CharField(max_length=10, primary_key=True,
                          verbose_name="Identificador")
    title = models.CharField(
        max_length=_title_max_length, verbose_name="Nombre")

    class Meta:
        verbose_name_plural = 'Unidad de negocio'

    def __str__(self):
        return f'{self.title}'

    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title']

    class Meta:
        verbose_name_plural = 'Unidad de Negocio'


class TypeOfTests(models.Model):
    id = models.CharField(max_length=10, primary_key=True,
                          verbose_name="Identificador")
    title = models.CharField(
        max_length=_title_max_length, verbose_name="Nombre")

    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title']

    class Meta:
        verbose_name_plural = "Tipo de pruebas"

    def __str__(self):
        return self.title


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length,
                             verbose_name="Nombre Proyecto")
    description = models.TextField(
        null=False, blank=False, verbose_name="Descripción")
    startDate = models.DateField(
        auto_created=True, auto_now_add=False, auto_now=False, verbose_name="Fecha de Inicio")
    reporter = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='reporter_user_p', verbose_name="Reportado por")
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name="Estado")
    priority = models.CharField(
        choices=_priorityChoices, max_length=10, verbose_name="Prioridad")
    productOwner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='productOwner_user_p', verbose_name="Dueño del producto")
    developer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='dev_user_p', verbose_name="Desarrollador")
    qa = models.ForeignKey(User, on_delete=models.PROTECT,
                           related_name='qa_user_p', verbose_name="Tester de Calidad")
    stakeHolder = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='stakeh_user_p', verbose_name="StakeHolder")
    assignedTo = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='assignedTo_user_p', verbose_name="Asignado a")
    version = models.IntegerField(verbose_name="Versión")
    businessUnit = models.ForeignKey(
        BusinessUnit, on_delete=models.PROTECT, verbose_name="Unidad de negocio")
    typeOfTests = models.ForeignKey(
        TypeOfTests, on_delete=models.PROTECT, verbose_name="Tipo de Prueba")

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description',
                        'priority', 'view_releases_link']

        def get_form(self, request, obj=None, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            # Si se está editando un registro existente y 'reporter' ya está establecido, no lo cambies
            if obj:
                form.base_fields['reporter'].widget.attrs['readonly'] = 'true'
                form.base_fields['reporter'].disabled = True
            else:
                # Si se está creando un nuevo registro, asigna el usuario actual automáticamente
                form.base_fields['reporter'].initial = request.user
                form.base_fields['reporter'].widget.attrs['readonly'] = True
                form.base_fields['reporter'].disabled = True
            # esto permite que en el campo po solo aparezcan los del grupo po
            group_users = User.objects.filter(groups__name=pownerGroup)
            # print(group_users)
            # self.fields['productOwner'].queryset = group_users
            # self.fields['productOwner'].widget = FilteredSelectMultiple('Usuarios', False)

            group_usersDev = User.objects.filter(groups__name=devGroup)
            # self.fields['developer'].queryset = group_usersDev
            # self.fields['developer'].widget = FilteredSelectMultiple('Usuarios', False)
            return form

        def view_releases_link(self, obj):
            count = obj.release_set.count()
            url = (reverse("admin:core_release_changelist")
                   + "?"
                   + urlencode({"project__id": f"{obj.id}"})
                   )
            return count

    class Meta:
        verbose_name_plural = "Proyectos"


class Release(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length,
                             verbose_name="Nombre de Entrega")
    description = models.TextField(verbose_name="Descripción")
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, verbose_name="Proyecto")
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name="Estado")
    reporter = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='reporter_user', verbose_name="Creado por")
    """el id de quien crea la incidencia """
    assignedTo = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='assignedTo', verbose_name="Asignado a")
    """cuando escriba el inicio del nombre le estire las opciones de users ya creados"""
    priority = models.CharField(
        max_length=10, choices=_priorityChoices, verbose_name="Prioridad")
    version = models.IntegerField(verbose_name="Versión")
    typeOfTests = models.ForeignKey(
        TypeOfTests, on_delete=models.PROTECT, verbose_name="Tipo de Prueba")
    qaDeploymentPlanningDate = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha planificada despliegue QA")
    testPlanCreationDate = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha de creación del plan de pruebas")
    testStartDate = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha de inicio de pruebas")
    testEndDate = models.DateField(auto_now=False, auto_now_add=False,
                                   blank=True, verbose_name="Fecha de finalización de pruebas")
    plannedImplementationDate = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha planificada de Implementación")
    finalImplementationDate = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, verbose_name="Fecha de implementación")
    productOwner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='productOwner_user', verbose_name="Dueño del producto")
    developer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='dev_user', verbose_name="Desarrollador")
    qa = models.ForeignKey(User, on_delete=models.PROTECT,
                           related_name='qa_user', verbose_name="Tester")
    last_update = models.DateTimeField(
        auto_created=True, auto_now=True)
    # releaseCommercialApproval = models.ForeignKey(ReleaseCommercialApproval, on_delete=models.PROTECT)
    # businessAreaAffected = models.ForeignKey(BusinessAreaAffected)

    def __str__(self):
        return f'{self.id} - {self.title}'

    no_admin = True

    class Admin(admin.ModelAdmin):
        def get_form(self, request, obj=None, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            # Si se está editando un registro existente y 'usuario_asignado' ya está establecido, no lo cambies
            if obj:
                form.base_fields['reporter'].widget.attrs['readonly'] = 'true'
                form.base_fields['reporter'].disabled = True
            else:
                # Si se está creando un nuevo registro, asigna el usuario actual automáticamente
                form.base_fields['reporter'].initial = request.user
                form.base_fields['reporter'].widget.attrs['readonly'] = True
                form.base_fields['reporter'].disabled = True
            return form

    class Meta:
        verbose_name_plural = "Entregas"


class Platform(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    title = models.CharField(max_length=_title_max_length,
                             verbose_name="Nombre Plataforma")
    link = models.CharField(
        max_length=300, verbose_name="Link de la plataforma")

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name_plural = "Plataformas"


class ReleasePlatformAffected(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    release = models.ForeignKey(
        Release, on_delete=models.PROTECT, verbose_name="Entrega relacionada")
    platform = models.ForeignKey(
        Platform, on_delete=models.PROTECT, verbose_name="Plataforma Afectada")

    def __str__(self):
        return f'{self.release}'

    class Meta:
        verbose_name_plural = "Plataforma afectada por la Entrega"


class BusinessAreaAffected (models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    areaAffected = models.CharField(
        max_length=_title_max_length, verbose_name="Área afectada")

    def __str__(self):
        return f'{self.id} - {self.areaAffected}'

    class Meta:
        verbose_name_plural = "Área del negocio afectada"


class ReleaseCommercialApproval(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    businessAreaAffected = models.ForeignKey(
        BusinessAreaAffected, on_delete=models.PROTECT, verbose_name="Área del negocio afectada")
    approved = models.BooleanField(default=False, verbose_name="Aprobado")
    release = models.ForeignKey(
        Release, on_delete=models.PROTECT, verbose_name="Entrega relacionada")

    no_admin = True

    class Meta:
        verbose_name_plural = "Aprobación comercial de la entrega"


class TypeTask(models.Model):
    id = models.CharField(max_length=10, primary_key=True,
                          verbose_name="Identificador")
    title = models.CharField(max_length=_title_max_length,
                             verbose_name="Nombre tipo tarea")

    def __str__(self) -> str:
        return f"{self.id} | {self.title}"

    class Meta:
        verbose_name_plural = "Tipo de Tarea"


class Task(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    title = models.CharField(
        max_length=_title_max_length, verbose_name="Nombre Tarea")
    typeTask = models.ForeignKey(
        TypeTask, on_delete=models.PROTECT, verbose_name="Tipo de Tarea")
    associatedRealease = models.ForeignKey(
        Release, on_delete=models.PROTECT, verbose_name="Entrega relacionada")
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name="Estado")
    assignedTo = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Asignado a")
    description = models.TextField(verbose_name="Descripción")
    comments = models.TextField(verbose_name="Comentarios")

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name_plural = "Tareas"


class QaDocumentation(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    TestPlans = models.TextField(verbose_name="Nombre del Plan de Pruebas")
    productOwnerApproval = models.BooleanField(
        default=False, verbose_name="Aprobación del Dueño del producto")
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name="Estado")
    """esto podria ser por ejemplo un check que solo tenga permiso de modificar ese perfil? para ahorrar tiempo en no enviar correos?"""
    developerApproval = models.BooleanField(
        default=False, verbose_name="Aprobación del Desarrollador")
    impTC = (('BAJA', 'Baja'),
             ('MED', 'Media'),
             ('ALTA', 'Alta')
             )
    importanceOfTestCases = models.CharField(
        max_length=10, choices=impTC, verbose_name="Importancia de los casos de PRueba")
    evidenceOfTheTestPlans = models.TextField(
        verbose_name="Evidencias del plan de pruebas")
    # ChecklistTestTypes = models.ForeignKey(ChecklistDocumentation, on_delete=models.PROTECT)

    no_admin = True

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name_plural = "Documentaciones QA"


class ChecklistDocumentation (models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    typeOfTests = models.ForeignKey(
        TypeOfTests, on_delete=models.PROTECT, verbose_name="Tipos de prueba")
    releasePlatformAffected = models.ForeignKey(
        ReleasePlatformAffected, on_delete=models.PROTECT, verbose_name="Entrega relacionada")
    qaDocumentation = models.ForeignKey(
        QaDocumentation, on_delete=models.PROTECT, verbose_name="Documentación QA")

    no_admin = True

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name_plural = "Lista de Verificación de Documentaciones"


class ReportedBugs(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    title = models.CharField(max_length=_title_max_length,
                             verbose_name="Título del error")
    typeInput = models.CharField(
        max_length=300, verbose_name="Descripción del Error")
    reporter = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='reporter_bug_user', null=True, verbose_name="Reportado por")
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT,
                                   related_name='bug_assignedto_user', null=True, verbose_name="Asignado a")
    statusBugs_choices = (('New', 'Nuevo'),
                          ('MoreData', 'Es necesaria más información'),
                          ('Assig', 'Asignado'),
                          ('Resolv', 'Resuelto'),
                          ('Close', 'Cerrado'))
    status = models.CharField(
        max_length=10, choices=statusBugs_choices, verbose_name="Estado del Reporte")
    category_choices = (('NoDisp', 'Funcionalidad no disponible'),
                        ('Handling', 'Manejo de errores definidos'),
                        ('IncImp', 'Implementación incorrecta'),
                        ('improve', 'Mejora'),
                        ('Secure', 'Error de Seguridad'),
                        ('UserInt', 'Interfaz de usuario'),
                        ('Usab', 'Usabilidad'),
                        ('Navi', 'Navigabilidad'))
    category = models.CharField(
        max_length=10, choices=category_choices, verbose_name="Categoría")
    priority_choices = (('Block', 'Bloqueado'),
                        ('Urg', 'Urgente'),
                        ('High', 'Alto'),
                        ('Ave', 'Medio'),
                        ('Low', 'Bajo'))
    priority = models.CharField(
        max_length=10, choices=priority_choices,  verbose_name="Prioridad")
    severity_choices = (('Cri', 'Crítico'),
                        ('Ma', 'Mayor'),
                        ('Mi', 'Menor'),
                        ('Sug', 'Sugerencia'))
    severity = models.CharField(
        max_length=10, choices=severity_choices,  verbose_name="Severidad")
    frenquency_choices = (('Alw', 'Siempre'),
                          ('Som', 'A veces'),
                          ('Rand', 'Aleatorio'),
                          ('NotTri', 'No se ha intentado'),
                          ('NotRep', 'No reproducible'),
                          ('Unknown', 'Desconocido'))
    frenquency = models.CharField(max_length=10, choices=frenquency_choices,  verbose_name="Frecuencia")
    summary = models.CharField(max_length=50,  verbose_name="Resumen del error")
    description = models.TextField( verbose_name="Descripción")
    stepsToReproduce = models.TextField( verbose_name="Pasos para replicar")

    class Meta:
        verbose_name_plural = 'Reporte de Errores'

    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'typeInput', 'reporter', 'assignedTo']

        def get_form(self, request, obj=None, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            # Si se está editando un registro existente y 'usuario_asignado' ya está establecido, no lo cambies
            if obj:
                form.base_fields['reporter'].widget.attrs['readonly'] = True
                form.base_fields['reporter'].disabled = True
            else:
                # Si se está creando un nuevo registro, asigna el usuario actual automáticamente
                form.base_fields['reporter'].initial = request.user
            return form
    """subir archivos se podria? por ejemplo print de pantalla, videos"""


class ImplementationRelease(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    description = models.TextField(verbose_name="Descripción")
    idRelease = models.ForeignKey(
        Release, on_delete=models.PROTECT, verbose_name="Entrega relacionada")
    ImplementationDate = models.DateField(
        verbose_name="Fecha de Implementación")
    Documentation = models.ForeignKey(
        QaDocumentation, on_delete=models.PROTECT, verbose_name="Documentación")
    developerInCharge = models.TextField(verbose_name="Desarrollador a cargo")
    qaInCharge = models.TextField(verbose_name="Tester a cargo")
    results = models.TextChoices("Exitoso", "Fallido")
    descriptionResults = models.TextField(
        verbose_name="Descripción de resultados")
    # Testejecution = models.ForeignKey(TestEjecution, on_delete=models.PROTECT)
    testEvidence = models.CharField(
        max_length=50, verbose_name="Evidencias de las pruebas")
    """poder adjuntar imagenes, videos"""

    class Meta:
        verbose_name_plural = "Implementación de la Entrega"

    class Admin(admin.ModelAdmin):
        list_display = ['id', 'description', 'idRelease',
                        'ImplementationDate', 'view_testexe_link']

        def view_testexe_link(self, obj):
            count = obj.textejecution_set.count()
            url = (reverse("admin:core_testejecution_changelist")
                   + "?"
                   + urlencode({"implementationrelease__id": f"{obj.id}"})
                   )

    def __str__(self) -> str:
        return f"{self.id} | {self.description}"


class TestEjecution(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    title = models.CharField(max_length=100, verbose_name="Título")
    generalDescription = models.TextField(verbose_name="Descripción general")
    # CaseTest = models.ForeignKey(CaseTest, on_delete=models.PROTECT)
    implementationRelease = models.ForeignKey(
        ImplementationRelease, on_delete=models.PROTECT, verbose_name="Entrega relacionada")

    no_admin = True

    class Meta:
        verbose_name_plural = "Ejecución de Pruebas"

    def __str__(self):
        return f'{self.id} - {self.title}'


class CaseTest(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    title = models.CharField(
        max_length=40, verbose_name="Nombre del caso de prueba")
    caseTestDescription = models.TextField(verbose_name="Descripción")
    caseTestPreconditions = models.TextField(verbose_name="Precondiciones")
    caseOrder = models.PositiveIntegerField(
        verbose_name="Orden del caso de prueba")
    caseSteps = models.TextField(verbose_name="Pasos a seguir")
    caseExpectedOutcome = models.TextField(verbose_name="Resultado Esperado")
    testEjecution = models.ForeignKey(
        TestEjecution, on_delete=models.PROTECT, verbose_name="Plan de pruebas relacionado")

    def __str__(self):
        return f'{self.id} - {self.title}'

    # no_admin = True

    class Meta:
        verbose_name_plural = "Caso de Prueba"


class QaDocumentationCaseTestImp(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    caseTest = models.ForeignKey(
        CaseTest, on_delete=models.PROTECT, verbose_name="Caso de prueba")
    qaDocumentation = models.ForeignKey(
        QaDocumentation, on_delete=models.PROTECT, verbose_name="Documentación QA")
    impTC = (('BAJA', 'Baja'),
             ('MED', 'Media'),
             ('ALTA', 'Alta')
             )
    importanceOfTestCases = models.CharField(
        max_length=10, choices=impTC, verbose_name="Importancia de los casos de prueba")

    class Meta:
        verbose_name_plural = "Importancia de los casos de prueba en las Documentaciones QA"


"""
Preguntas
1- para enviar notificaciones a las personas cuando cambia de estado un error?
3- en que parte se agrega el buscador? en cada tabla o se hace una tabla aparte? Seria esto mas o menos:
search: id_Proyectos, id_Entregas, id_Incidencias, id_EstadoIncidencias, id_PersonaAsignada, 
chartlenght_Proyectos, chartlenght_Entregas, chartlenght_Incidencias, chartlenght_EstadoIncidencias, 
chartlenght_PersonaAsignada.

"""
