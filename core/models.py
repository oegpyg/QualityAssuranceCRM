from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.contrib.auth.models import User


_title_max_length = 100
class Status(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50, blank=False, null=False)
    target_flow = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id} | {self.label}"
    
    class Admin(admin.ModelAdmin):
        search_fields = ['label', 'target_flow']
        list_filter = ['target_flow']
        list_display = ['id', 'label', 'target_flow']

class StatusHistory(models.Model):
    """To manage changes history of any records"""
    id = models.AutoField(primary_key=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    record = models.CharField(max_length=20)
    record_id =  models.IntegerField(null=False, blank=False)
    transDate = models.DateTimeField(auto_now=True, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=300)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    description = models.TextField(null=False, blank=False)
    """se puede poner como un campo obligatorio de historia de usuario?"""
    startDate = models.DateField(auto_created=True, auto_now_add=False, auto_now=False)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    """ tendria que ser el id de quien crea la incidencia """
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    priority_choices = (('BAJ', 'BAJA'),
                        ('MED', 'MEDIA'),
                        ('ALT', 'ALTA'))
    priority = models.TextField(choices=priority_choices) #debe ser una tabla coloco como ejemplo choices
    """ se podria setear especificos?, ejemplo: alta, media, baja """
    productOwner = models.ForeignKey(User, on_delete=models.PROTECT)
    developer = models.ForeignKey(User, on_delete=models.PROTECT)
    qa = models.ForeignKey(User, on_delete=models.PROTECT)
    stakeholder = models.ForeignKey(User, on_delete=models.PROTECT)
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT)
    version = models.IntegerField()
    businessUnit = models.CharField() #deberia ser una tabla
    TypeOfTests = models.TextField() #deberia ser una tabla? 
    """ se podria setear especificos?, ejemplo: end2end, unitarias, UAT, rendimiento, integración, monitoreo, seguridad, migracion de datos """

    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description', 'priority', 'view_releases_link']

        def view_releases_link(self, obj):
          count = obj.release_set.count()
          url = (
                    reverse("admin:core_release_changelist")
                  + "?"
                  + urlencode({"project__id": f"{obj.id}"})
                 )


class Release(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    """ tendria que ser el id de quien crea la incidencia """
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT)
    """como hacer que cuando escriba el inicio del nombre le estire las opciones de users ya creados?"""
    priority = models.TextField() #debe ser una tabla  
    """ se podria setear especificos?, ejemplo: alta, media, baja """
    version = models.IntegerField()
    TypeOfTests = models.TextField() #debe ser una tabla  
    """ se podria setear especificos?, ejemplo: end2end, unitarias, UAT, rendimiento, integración, monitoreo, seguridad, migracion de datos """
    QaDeploymentPlanningDate = models.DateField(auto_now=False, auto_now_add=False)
    TestPlanCreationDate= models.DateField(auto_now=False, auto_now_add=False)
    TestStartDate = models.DateField(auto_now=False, auto_now_add=False)
    TestEndDate = models.DateField(auto_now=False, auto_now_add=False)
    plannedImplementationDate= models.DateField(auto_now=False, auto_now_add=False)
    finalImplementationDate= models.DateField(auto_now=False, auto_now_add=False)
    productOwner = models.ForeignKey(User, on_delete=models.PROTECT)
    developer = models.ForeignKey(User, on_delete=models.PROTECT)
    qa = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description', 'plannedImplementationDate', 'finalImplementationDate']

class ReleasePlatformAffected(models.Model):
    id = models.AutoField(primary_key=True)
    release = models.ForeignKey(Release, on_delete=models.PROTECT)
    platform   = models.ForeignKey(Platform, on_delete=models.PROTECT) #debes tener una tabla de plataformas y este debe ser tipo detalle

class ReleaseCommercialApproval(models.Model):
    BusinessAreaAffected = models.CharField(max_length=100) #considerar tabla
    Approved = models.BooleanField(default=False)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    typeTask = models.CharField(max_length=50) #debe ser tabla
    """En alguna parte se tendria que poder crear y elegir el tipo por ejemplo tarea, historia de usuario"""
    AssociatedRealease = models.ForeignKey(Release, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    comments = models.TextField()

class QaDocumentation(models.Model):
    id = models.AutoField(primary_key=True)
    TestPlans = models.TextField()
    ProductOwnerApproval = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    """esto podria ser por ejemplo un check que solo tenga permiso de modificar ese perfil? para ahorrar tiempo en no enviar correos?"""
    DeveloperApproval = models.BooleanField(default=False)
    ImportanceOfTestCases = models.TextField()
    ChecklistTestTypes = models.TextField()
    EvidenceOfTheTestPlans = models.TextField()
    
class ReportedBugs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
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