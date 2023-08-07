#from msilib import typemask
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.contrib.auth.models import User


_title_max_length = 100
_priorityChoices = (('BAJ', 'BAJA'),
                    ('MED', 'MEDIA'),
                    ('ALT', 'ALTA'))
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
    transDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class BusinessUnit(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=_title_max_length)

    def __str__(self):
        return f'{self.id} - {self.title}'
    


    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title']
    
    class Meta:
        verbose_name_plural = 'Business Unit'
    
class TypeOfTests(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title']
    
    class Meta:
        verbose_name_plural = "Type of Tests"

    def __str__(self):
        return self.title


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    description = models.TextField(null=False, blank=False)
    startDate = models.DateField(auto_created=True, auto_now_add=False, auto_now=False)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reporter_user_p')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    priority = models.CharField(choices=_priorityChoices, max_length=10)
    productOwner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='productOwner_user_p')
    developer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='dev_user_p')
    qa = models.ForeignKey(User, on_delete=models.PROTECT, related_name='qa_user_p')
    stakeHolder = models.ForeignKey(User, on_delete=models.PROTECT, related_name='stakeh_user_p')
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assignedTo_user_p')
    version = models.IntegerField()
    businessUnit = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT)
    typeOfTests = models.ForeignKey(TypeOfTests, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description', 'priority', 'view_releases_link']
        
        def view_releases_link(self, obj):
          count = obj.release_set.count()
          url = (reverse("admin:core_release_changelist")
                  + "?"
                  + urlencode({"project__id": f"{obj.id}"})
                 )


class Release(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reporter_user')
    """el id de quien crea la incidencia """
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assignedTo')
    """cuando escriba el inicio del nombre le estire las opciones de users ya creados"""
    priority = models.CharField(max_length=10, choices=_priorityChoices)
    version = models.IntegerField()
    typeOfTests = models.ForeignKey(TypeOfTests, on_delete=models.PROTECT)
    qaDeploymentPlanningDate = models.DateField(auto_now=False, auto_now_add=False)
    testPlanCreationDate= models.DateField(auto_now=False, auto_now_add=False)
    testStartDate = models.DateField(auto_now=False, auto_now_add=False)
    testEndDate = models.DateField(auto_now=False, auto_now_add=False)
    plannedImplementationDate= models.DateField(auto_now=False, auto_now_add=False)
    finalImplementationDate= models.DateField(auto_now=False, auto_now_add=False)
    productOwner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='productOwner_user')
    developer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='dev_user')
    qa = models.ForeignKey(User, on_delete=models.PROTECT, related_name='qa_user')
    #releaseCommercialApproval = models.ForeignKey(ReleaseCommercialApproval, on_delete=models.PROTECT)
    #businessAreaAffected = models.ForeignKey(BusinessAreaAffected)


    def __str__(self):
        return f'{self.id} - {self.title}'
    
    no_admin = True

class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    link = models.CharField(max_length=300)

class ReleasePlatformAffected(models.Model):
    id = models.AutoField(primary_key=True)
    release = models.ForeignKey(Release, on_delete=models.PROTECT)
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT) 


class BusinessAreaAffected (models.Model):
    id = models.AutoField(primary_key=True)
    areaAffected = models.CharField(max_length=_title_max_length)

class ReleaseCommercialApproval(models.Model):
    id = models.AutoField(primary_key=True)
    businessAreaAffected = models.ForeignKey(BusinessAreaAffected, on_delete=models.PROTECT)
    approved = models.BooleanField(default=False)
    release = models.ForeignKey(Release, on_delete=models.PROTECT)

    no_admin = True



class TypeTask(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=_title_max_length)

    class Meta:
        verbose_name_plural = "Type Task"

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    typeTask = models.ForeignKey(TypeTask, on_delete=models.PROTECT)
    associatedRealease = models.ForeignKey(Release, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    assignedTo = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    comments = models.TextField()



class QaDocumentation(models.Model):
    id = models.AutoField(primary_key=True)
    TestPlans = models.TextField()
    productOwnerApproval = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    """esto podria ser por ejemplo un check que solo tenga permiso de modificar ese perfil? para ahorrar tiempo en no enviar correos?"""
    developerApproval = models.BooleanField(default=False)
    impTC = (('BAJA', 'Baja'),
             ('MED', 'Media'),
             ('ALTA', 'Alta')
             )
    importanceOfTestCases = models.CharField(max_length=10, choices=impTC)
    #ChecklistTestTypes = models.ForeignKey(ChecklistDocumentation, on_delete=models.PROTECT)
    evidenceOfTheTestPlans = models.TextField()

    no_admin = True

class ChecklistDocumentation (models.Model):
    id = models.AutoField(primary_key=True)
    typeOfTests = models.ForeignKey(TypeOfTests, on_delete=models.PROTECT)
    releasePlatformAffected = models.ForeignKey(ReleasePlatformAffected, on_delete=models.PROTECT)
    qaDocumentation = models.ForeignKey(QaDocumentation, on_delete=models.PROTECT)

    no_admin = True

class ReportedBugs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=_title_max_length)
    typeInput = models.CharField(max_length=100)
    reportedBy = models.CharField(max_length=100)
    """deberia aceptar solo usuarios creados"""
    assignedTo = models.TextField()
    """deberia aceptar solo usuarios creados"""
    statusBugs_choices = (('New', 'New'),
                ('MoreData', 'More data is needed'),
                ('Assig', 'Assigned'),
                ('Resolv', 'Resolved'),
                ('Close', 'Close'))
    status = models.CharField(max_length=10, choices=statusBugs_choices)
    category_choices = (('NoDisp', 'Functionality Not Available'),
                ('Handling', 'Error Handling'),
                ('IncImp', 'Incorrect Implementation'),
                ('improve', 'Improvement'),
                ('Secure', 'Security'),
                ('UserInt', 'User Interface'),
                ('Usab', 'Usability'),
                ('Navi', 'Navigability'))
    category = models.CharField(max_length=10, choices=category_choices)
    priority_choices = (('Block', 'Blocking'),
                        ('Urg', 'Urgent'),
                        ('High', 'High'),
                        ('Ave', 'Average'),
                        ('Low', 'Low'))
    priority = models.CharField(max_length=10, choices=priority_choices)
    severity_choices = (('Cri', 'Critical'),
                ('Ma', 'Major'),
                ('Mi', 'Minor'),
                ('Sug', 'Suggestion'))
    severity = models.CharField(max_length=10, choices=severity_choices)
    frenquency_choices = (('Alw', 'Always'),
                          ('Som', 'Sometimes'),
                          ('Rand', 'Random'),
                          ('NotTri', 'Not Tried'),
                          ('NotRep', 'Not Reproducible'),
                          ('Unknown', 'Unknown'))
    frenquency = models.CharField(max_length=10, choices=frenquency_choices)
    summary = models.CharField(max_length=50)
    description = models.TextField()
    stepsToReproduce = models.TextField()

    """subir archivos se podria? por ejemplo print de pantalla, videos"""

class ImplementationRelease(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    idRelease = models.ForeignKey(Release, on_delete=models.PROTECT)
    ImplementationDate= models.DateField()
    Documentation = models.ForeignKey(QaDocumentation, on_delete=models.PROTECT)
    developerInCharge = models.TextField()
    qaInCharge = models.TextField()
    results = models.TextChoices("Exitoso", "Fallido")
    descriptionResults = models.TextField()
    #Testejecution = models.ForeignKey(TestEjecution, on_delete=models.PROTECT)
    testEvidence = models.CharField(max_length=50)
    """poder adjuntar imagenes, videos"""
    class Meta:
        verbose_name_plural = "Implementation Release"
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'description', 'idRelease', 'ImplementationDate', 'view_testexe_link']
        
        def view_testexe_link(self, obj):
          count = obj.textejecution_set.count()
          url = (reverse("admin:core_testejecution_changelist")
                  + "?"
                  + urlencode({"implementationrelease__id": f"{obj.id}"})
                 )

class TestEjecution(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    generalDescription = models.TextField()
    #CaseTest = models.ForeignKey(CaseTest, on_delete=models.PROTECT)
    implementationRelease = models.ForeignKey(ImplementationRelease, on_delete=models.PROTECT)

    no_admin = True
    class Meta:
        verbose_name_plural = "Test Execution"

class CaseTest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    caseTestDescription = models.TextField()
    caseTestPreconditions = models.TextField()
    caseOrderSteps = models.IntegerField()
    caseSteps = models.TextField()
    caseExpectedOutcome = models.TextField()
    testEjecution = models.ForeignKey(TestEjecution, on_delete=models.PROTECT)

    no_admin = True

    class Meta:
        verbose_name_plural = "Case Test"

class QaDocumentationCaseTestImp(models.Model):
    id = models.AutoField(primary_key=True)
    caseTest = models.ForeignKey(CaseTest, on_delete=models.PROTECT)
    qaDocumentatio = models.ForeignKey(QaDocumentation, on_delete=models.PROTECT)
    impTC = (('BAJA', 'Baja'),
             ('MED', 'Media'),
             ('ALTA', 'Alta')
             )
    importanceOfTestCases = models.CharField(max_length=10, choices=impTC)


"""
Preguntas
1- para enviar notificaciones a las personas cuando cambia de estado un error?
3- en que parte se agrega el buscador? en cada tabla o se hace una tabla aparte? Seria esto mas o menos:
search: id_Proyectos, id_Entregas, id_Incidencias, id_EstadoIncidencias, id_PersonaAsignada, 
chartlenght_Proyectos, chartlenght_Entregas, chartlenght_Incidencias, chartlenght_EstadoIncidencias, 
chartlenght_PersonaAsignada.

"""