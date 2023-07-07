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



class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    fecha_inicio = models.DateField()
    """usuario 
    techlead
    owner
    developer
    architech""" 

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
            return format_html('<a href="{}">{} Releases</a>', url, count)

class Release(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignedTo
    
    def __str__(self):
        return f'{self.id} - {self.title}'
    
    class Admin(admin.ModelAdmin):
        list_display = ['id', 'title', 'description']

"""
Tablas
PerfilUsuarios: id, chartlenght, permisos?
 Usuarios: id, chartlenght, user, password, id_PerfilUsuarios
Proyectos: id, chartlenght, id_entregas, id_EstadoIncidencias……. creador, estado, prioridad, asignado a, versión, unidad de negocio, tipos de pruebas (end2end, rendimiento, usabilidad, portabilidad),líder técnico, solicitante. 
Entregas: id, chartlenght, id_Proyectos, id_EstadoIncidencias……. creador, estado, prioridad, asignado a, versión, unidad de negocio, link evidencias, plataformas afectadas (app mobile, app web, crm1, crm2, base de datos X) , área de prueba (digital, x, y), tipos de pruebas (end2end, rendimiento, usabilidad, portabilidad), planificación despliegue en QA, fecha de implementación planificada, fecha implementación final, líder técnico, solicitante, aprobación comercial necesaria.
    Tipo_Entrada:  id, chartlenght.
Incidencias: id, chartlenght, id_Estado_Incidencias
EstadoIncidencias:  id, chartlenght, id_incidencias
Histórico_estados:  id, chartlenght, id_EstadoIncidencias
    PersonaAsignada: id, chartlenght 
CampoComentarios: chartlenght, id_incidencias 
DocumentacionProyecto: id, chartlenght, historias de usuario
DocumentacionEntrega: id, chartlenght, documentaciones qa? plan de pruebas, aprobación del plan de pruebas, checklist tipos de pruebas, importancia de casos de prueba, evidencias, cierre, planilla de riesgos.  
ErroresReportados:  id, chartlenght, detalle, responsable, campo para adjuntar imagen??
    Estado_Error:  id, chartlenght, id_ErroresReportados
Implementación_producción:  id, chartlenght, date?, id_DocumentaciónEntrega, resultado?, id_usuarios (a cargo) 
search: id_Proyectos, id_Entregas, id_Incidencias, id_EstadoIncidencias, id_PersonaAsignada, chartlenght_Proyectos, chartlenght_Entregas, chartlenght_Incidencias, chartlenght_EstadoIncidencias, chartlenght_PersonaAsignada.



Preguntas
1- para la parte en donde se carguen las evidencias tambien se necesitarian tablas?
2- para enviar notificaciones a las personas cuando cambia de estado un error?



class Buscador? (admin.ModelBuscador):









models: crear tablas necesarias PRIMERO
para crear tablas es en models.py
class ProductAdmin(admin.ModelAdmin):
search_algo para buscar
lostfilter: filtrar
list_display: son columnas que se listan en el menu principal

en admin
admin.site.register(nombre de la clase de la tabla)


"""