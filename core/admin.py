from django.contrib import admin
from django.apps import apps
from .models import ReleaseCommercialApproval, Release, QaDocumentation, ChecklistDocumentation, TestEjecution, CaseTest

nombre_aplicacion = 'core'

# Obtiene todos los modelos registrados en la aplicación especificada
modelos = apps.get_app_config(nombre_aplicacion).get_models()

# Registra todos los modelos en el administrador
for modelo in modelos:
    if 'no_admin' not in modelo.__dict__:
        if 'Admin' in modelo.__dict__:
            admin.site.register(modelo, modelo.Admin)
        else:
            admin.site.register(modelo)

class ReleaseCommercialApprovalAdminTabular(admin.TabularInline):
    model = ReleaseCommercialApproval
    extra = 1
class ReleaseAdmin(admin.ModelAdmin):
        list_filter = ['project']
        list_display = ['id', 'title', 'description', 'plannedImplementationDate', 'finalImplementationDate']
        inlines = [ReleaseCommercialApprovalAdminTabular, ]

admin.site.register(Release, ReleaseAdmin)

class ChecklistDocumentationAdminTabular(admin.TabularInline):
     model = ChecklistDocumentation
     extra = 1

class QaDocumentationAdmin(admin.ModelAdmin):
     list_display = ['id', 'TestPlans', 'productOwnerApproval', 'developerApproval', 'status']
     inlines = [ChecklistDocumentationAdminTabular, ]

admin.site.register(QaDocumentation, QaDocumentationAdmin)

class CaseTestAdminTabular(admin.TabularInline):
     model = CaseTest
     extra = 1

class TestEjecutionAdmin(admin.ModelAdmin):
     list_display = ['id', 'title', 'implementationRelease', 'generalDescription']
     inlines = [CaseTestAdminTabular, ]

admin.site.register(TestEjecution, TestEjecutionAdmin)

