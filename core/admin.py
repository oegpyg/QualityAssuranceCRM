from django.contrib import admin
from django.apps import apps
from .models import ReleaseCommercialApproval, Release, QaDocumentation, ChecklistDocumentation, TestEjecution, CaseTest, QaDocumentationCaseTestImp
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

nombre_aplicacion = 'core'
devGroup = 'Developer'
pownerGroup = 'ProductOwner'
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

class QaDocumentationCaseTestImpAdminTabular(admin.TabularInline):
     model = QaDocumentationCaseTestImp
     extra = 1 

class QaDocumentationForm(forms.ModelForm):
     class Meta:
          model = QaDocumentation
          fields = ['id', 'TestPlans', 'productOwnerApproval', 'developerApproval', 'status']
     
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)    
          user = self.request.user
          if user and not user.groups.filter(name=pownerGroup).exists():
               self.fields['productOwnerApproval'].widget.attrs['disabled'] = 'disabled'
          if user and not user.groups.filter(name=devGroup).exists():
               self.fields['developerApproval'].widget.attrs['disabled'] = 'disabled'

class QaDocumentationAdmin(admin.ModelAdmin):
     def get_form(self, request, obj=None, **kwargs):
          form = super().get_form(request, obj, **kwargs)
          form.request = request
          return form
     form = QaDocumentationForm
     inlines = [ChecklistDocumentationAdminTabular, QaDocumentationCaseTestImpAdminTabular]

admin.site.register(QaDocumentation, QaDocumentationAdmin)

class CaseTestAdminTabular(admin.TabularInline):
     model = CaseTest
     extra = 1

class TestEjecutionAdmin(admin.ModelAdmin):
     list_display = ['id', 'title', 'implementationRelease', 'generalDescription']
     inlines = [CaseTestAdminTabular, ]

admin.site.register(TestEjecution, TestEjecutionAdmin)



class GroupFilter(admin.SimpleListFilter):
     title = 'Grupo'  # El título que se mostrará en la interfaz de administración
     parameter_name = 'group'  # El nombre del parámetro en la URL

     def lookups(self, request, model_admin):
         # Devuelve una lista de opciones de filtro (id, nombre)
         groups = User.objects.values_list('groups__id', 'groups__name').distinct()
         return groups

     def queryset(self, request, queryset):
         # Aplica el filtro a la consulta
         if self.value():
             return queryset.filter(groups__id=self.value())

class UserAdmin(admin.ModelAdmin):
     list_filter = (GroupFilter,)
     list_display = ['username', 'first_name', 'last_name', 'access_group']
     #filter_horizontal = ("permissions",)
     def access_group(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

