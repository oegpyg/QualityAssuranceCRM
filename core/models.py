from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50, blank=False, null=False)
    target_flow = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.id} | {self.label}"
    
    class Admin(admin.ModelAdmin):
        search_fields = ['label', 'target_flow']
        list_filter = ['target_flow']
        list_display = ['id', 'label', 'target_flow']

class HistoricStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.ForeignKey(Status)
    

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    """se puede poner como un campo obligatorio de historia de usuario?"""
    startDate = models.DateField()
    creator = models.models.TextField()
    """ tendria que ser el id de quien crea la incidencia """
    status = models.ForeignKey(Status)
    priority = models.TextField()  
    """ se podria setear especificos?, ejemplo: alta, media, baja """
    productOwner = models.TextField()
    developer = models.TextField()
    qa = models.TextField()
    stakeholder = models.TextField() 
    assignedTo = models.TextField()
    """como hacer que cuando escriba el inicio del nombre le estire las opciones de users ya creados?"""
    version = models.enums ()
    businessUnit = models.CharField()
    TypeOfTests = models.TextField()  
    """ se podria setear especificos?, ejemplo: end2end, unitarias, UAT, rendimiento, integración, monitoreo, seguridad, migracion de datos """

    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description', 'view_releases_link']

        def view_releases_link(self, obj):
          count = obj.release_set.count()
          url = (
                    reverse("admin:core_release_changelist")
                  + "?"
                  + urlencode({"project__id": f"{obj.id}"})
                 )
    

class Release(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(Status)
    creator = models.models.TextField()
    """ tendria que ser el id de quien crea la incidencia """
    assignedTo = models.TextField()
    """como hacer que cuando escriba el inicio del nombre le estire las opciones de users ya creados?"""
    priority = models.TextField()  
    """ se podria setear especificos?, ejemplo: alta, media, baja """
    version = models.enums ()
    businessUnit = models.CharField()
    LinkPlatform = models.FileField()
    PlatformAffected = models.CharField()
    TypeOfTests = models.TextField()  
    """ se podria setear especificos?, ejemplo: end2end, unitarias, UAT, rendimiento, integración, monitoreo, seguridad, migracion de datos """
    BusinessAreaAffected = models.CharField()
    """contabilidad, ventas, etc"""
    CommercialApproval = models.CharField(max_length=2)
    """si o no"""
    QaDeploymentPlanningDate = models.DateField()
    TestPlanCreationDate= models.DateField()
    TestStartDate = models.DateField()
    TestEndDate = models.DateField()
    PlannedImplementationDate= models.DateField()
    FinalImplementationDate= models.DateField()
    productOwner = models.TextField()
    """solo usuarios creados, no deberia de poder escribirse cualquier nombre"""
    developer = models.TextField()
    """solo usuarios creados, no deberia de poder escribirse cualquier nombre"""
    qa = models.TextField()
    """solo usuarios creados, no deberia de poder escribirse cualquier nombre"""

    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description']

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    email = models.EmailField()
    phonenumber = models.models.PhoneNumberField()
    profile = models.ForeignKey(perfilUsuarios)

class perfilUsuarios (models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()

class input (models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=50)
    TypeInput = models.CharField()
    """En alguna parte se tendria que poder crear y elegir el tipo por ejemplo tarea, historia de usuario"""
    AssociatedRealease = models.ForeignKey(Release)
    status = models.ForeignKey(Status)
    assignedTo = models.TextField()
    """como hacer que cuando escriba el inicio del nombre le estire las opciones de users ya creados?"""
    description = models.TextField()
    comments = models.models.TextField()

class QaDocumentation(models.Model):
    id = models.AutoField(primary_key=True)
    TestPlans = models.TextField()
    ProductOwnerApproval = models.TextField()
    """esto podria ser por ejemplo un check que solo tenga permiso de modificar ese perfil? para ahorrar tiempo en no enviar correos?"""
    DeveloperApproval = models.TextField()
    ImportanceOfTestCases = models.TextField()
    ChecklistTestTypes = models.TextField()
    EvidenceOfTheTestPlans = models.TextField()
    
class ReportedBugs(models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=50)
    TypeInput = models.CharField()
    ReportedBy = models.CharField()
    """deberia aceptar solo usuarios creados"""
    assignedTo = models.TextField()
    """mismo caso de solo usuarios creados"""
    StatusBugs = models.TextChoices("Nuevo", "Se necesitan más datos", "Asignado", "Resuelto", "Cerrado")
    Category = models.TextChoices("Funcionalidad no disponible", "Manejo de errores", "Implementacion incorrecta", "Mejora", "Observación", "Seguridad", "Interfaz de usuario", "Usabilidad", "Navegabilidad")
    Priority = models.TextChoices("Bloqueo", "Urgente", "Alta", "Media", "Baja")
    Severity = models.TextChoices("Crítico", "Mayor", "Menor", "Sugerencia")
    Reproducibility = models.TextChoices("Siempre", "A veces", "Aleatorio", "No se ha intentado", "No es reproducible", "Desconocido")
    Summary = models.CharField(max_length=50)
    Description = models.TextField()
    StepsToReproduce = models.TextField()
    """subir archivos se podria? por ejemplo print de pantalla, videos"""

class ImplementationRelease(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.models.TextField()
    idRelease = models.ForeignKey(Release)
    ImplementationDate= models.DateField()
    Documentation = models.models.models.ForeignKey(QaDocumentation)
    developerInCharge = models.TextField()
    qaInCharge = models.TextField()
    Results = models.TextChoices("Exitoso", "Fallido")
    DescriptionResults = models-models.TextField()
    TestEvidence = models.models.CharField(max_length=50)
    """poder adjuntar imagenes, videos"""

"""
Preguntas
1- para la parte en donde se carguen las evidencias tambien se necesitarian tablas?
2- para enviar notificaciones a las personas cuando cambia de estado un error?
3- en que parte se agrega el buscador? en cada tabla o se hace una tabla aparte? Seria esto mas o menos:
search: id_Proyectos, id_Entregas, id_Incidencias, id_EstadoIncidencias, id_PersonaAsignada, 
chartlenght_Proyectos, chartlenght_Entregas, chartlenght_Incidencias, chartlenght_EstadoIncidencias, 
chartlenght_PersonaAsignada.

"""