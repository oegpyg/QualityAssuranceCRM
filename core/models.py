from msilib import typemask
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

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    description = models.TextField(null=False, blank=False)
    startDate = models.DateField(auto_created=True, auto_now_add=False, auto_now=False)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    priority = models.ForeignKey(priorityChoices, on_delete=models.PROTECT)
    productOwner = models.ForeignKey(User, on_delete=models.PROTECT)
    developer = models.ForeignKey(User, on_delete=models.PROTECT)
    qa = models.ForeignKey(User, on_delete=models.PROTECT)
    stakeholder = models.ForeignKey(User, on_delete=models.PROTECT)
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT)
    version = models.IntegerField()
    businessUnit = models.ForeignKey(businessUnit, on_delete=models.PROTECT)
    TypeOfTests = models.ForeignKey(TypeOfTests, on_delete=models.PROTECT)

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

class priorityChoices(models.Model): 
priority = (('BAJ', 'BAJA'),
            ('MED', 'MEDIA'),
            ('ALT', 'ALTA'))

class businessUnit(models.Model):
businessUnit = (('B2C', 'Business to Consumer'),
                ('B2B', 'Business to Business'),
                ('C2C', 'Consumer to Consumer'),
                ('C2B', 'Cosumer to Business'),
                ('M2C', 'Mobile to Cosumer'),
                ('M2B', 'Mobile to Business'))

class TypeOfTests(models.Model):
    TypeOfTests = (('Unit', 'Unit Tests'),
                ('End2End', 'End2End'),
                ('Perf', 'Performance Tests'),
                ('ParRunn', 'Parallel Running Tests'),
                ('Available', 'Availability Tests'),
                ('Integ', 'Integration Tests'),
                ('Monit', 'Monitoring Tests'),
                ('Maintain', 'Maintainability Tests'),
                ('Security', 'Security Tests'),
                ('UAT', 'User Acceptance Testing'))

class Release(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT)
    """el id de quien crea la incidencia """
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT)
    """cuando escriba el inicio del nombre le estire las opciones de users ya creados"""
    priority = models.ForeignKey(priority_choices, on_delete=models.PROTECT)
    version = models.IntegerField()
    TypeOfTests = models.ForeignKey(TypeOfTests, on_delete=models.PROTECT)
    QaDeploymentPlanningDate = models.DateField(auto_now=False, auto_now_add=False)
    TestPlanCreationDate= models.DateField(auto_now=False, auto_now_add=False)
    TestStartDate = models.DateField(auto_now=False, auto_now_add=False)
    TestEndDate = models.DateField(auto_now=False, auto_now_add=False)
    plannedImplementationDate= models.DateField(auto_now=False, auto_now_add=False)
    finalImplementationDate= models.DateField(auto_now=False, auto_now_add=False)
    productOwner = models.ForeignKey(User, on_delete=models.PROTECT)
    developer = models.ForeignKey(User, on_delete=models.PROTECT)
    qa = models.ForeignKey(User, on_delete=models.PROTECT)
    ReleaseCommercialApproval = models.ForeignKey(ReleaseCommercialApproval, on_delete=models.PROTECT)
    BusinessAreaAffected = models.ForeignKey(BusinessAreaAffected)

    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description', 'plannedImplementationDate', 'finalImplementationDate']

class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=300)

class ReleasePlatformAffected(models.Model):
    id = models.AutoField(primary_key=True)
    release = models.ForeignKey(Release, on_delete=models.PROTECT)
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT) 

class ReleaseCommercialApproval(models.Model):
    BusinessAreaAffected = models.CharField(max_length=100)
    Approved = models.BooleanField(default=False)

class BusinessAreaAffected (models.Model):
    id = models.AutoField(primary_key=True)
    areaAffected = models.CharField()

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    TypeTask = models.ForeignKey(TypeTask, on_delete=models.PROTECT)
    AssociatedRealease = models.ForeignKey(Release, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    comments = models.TextField()

class TypeTask(models.Model):
    id = models.AutoField(primary_key=True)
    TypeTask = (('History', 'User History'),
                ('QA', 'QA Task'),
                ('Dev', 'Developer Task')
                ('Bugs', 'Bugs'))

class QaDocumentation(models.Model):
    id = models.AutoField(primary_key=True)
    TestPlans = models.TextField()
    ProductOwnerApproval = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    """esto podria ser por ejemplo un check que solo tenga permiso de modificar ese perfil? para ahorrar tiempo en no enviar correos?"""
    DeveloperApproval = models.BooleanField(default=False)
    ImportanceOfTestCases = models.TextField()
    ChecklistTestTypes = models.ForeignKey(ChecklistDocumentation, on_delete=models.PROTECT)
    EvidenceOfTheTestPlans = models.TextField()

class ChecklistDocumentation (models.Model):
    id = models.AutoField(primary_key=True)
    TypeOfTests = models.ForeignKey(TypeOfTests)
    ReleasePlatformAffected = models.ForeignKey(ReleasePlatformAffected)

class ReportedBugs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    TypeInput = models.CharField()
    ReportedBy = models.CharField()
    """deberia aceptar solo usuarios creados"""
    assignedTo = models.TextField()
    """deberia aceptar solo usuarios creados"""
    StatusBugs = (('New', 'New'),
                ('MoreData', 'More data is needed'),
                ('Assig', 'Assigned')
                ('Resolv', 'Resolved')
                ('Close', 'Close'))
    Category = (('NoDisp', 'Functionality Not Available'),
                ('Handling', 'Error Handling'),
                ('IncImp', 'Incorrect Implementation')
                ('improve', 'Improvement')
                ('Secure', 'Security')
                ('UserInt', 'User Interface')
                ('Usab', 'Usability')
                ('Navi', 'Navigability'))
    Priority = (('Block', 'Blocking'),
                ('Urg', 'Urgent'),
                ('High', 'High')
                ('Ave', 'Average')
                ('Low', 'Low'))
    Severity = (('Cri', 'Critical'),
                ('Ma', 'Major'),
                ('Mi', 'Minor')
                ('Sug', 'Suggestion'))
    Reproducibility = (('Alw', 'Always'),
                ('Som', 'Sometimes'),
                ('Rand', 'Random'),
                 ('NotTri', 'Not Tried'),
                ('NotRep', 'Not Reproducible')
                ('Unknown', 'Unknown'))
    Summary = models.CharField(max_length=50)
    Description = models.TextField()
    StepsToReproduce = models.TextField()
    """subir archivos se podria? por ejemplo print de pantalla, videos"""

class ImplementationRelease(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    idRelease = models.ForeignKey(Release)
    ImplementationDate= models.DateField()
    Documentation = models.ForeignKey(QaDocumentation)
    developerInCharge = models.TextField()
    qaInCharge = models.TextField()
    Results = models.TextChoices("Exitoso", "Fallido")
    DescriptionResults = models.TextField()
    Testejecution = models.ForeignKey(TestEjecution, on_delete=models.PROTECT)
    TestEvidence = models.CharField(max_length=50)
    """poder adjuntar imagenes, videos"""

class TestEjecution(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    GeneralDescription = models.TextField()
    CaseTest = models.ForeignKey(CaseTest, on_delete=models.PROTECT)

class CaseTest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    caseTestDescription = models.TextField()
    caseTestPreconditions = models.TextField()
    CaseOrderSteps = models.IntegerField()
    CaseSteps = models.TextField()
    CaseExpectedOutcome = models.TextField()

"""
Preguntas
1- para enviar notificaciones a las personas cuando cambia de estado un error?
3- en que parte se agrega el buscador? en cada tabla o se hace una tabla aparte? Seria esto mas o menos:
search: id_Proyectos, id_Entregas, id_Incidencias, id_EstadoIncidencias, id_PersonaAsignada, 
chartlenght_Proyectos, chartlenght_Entregas, chartlenght_Incidencias, chartlenght_EstadoIncidencias, 
chartlenght_PersonaAsignada.

"""