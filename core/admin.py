from django.contrib import admin
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    search_fields = ['label', 'target_flow']
    list_filter = ['target_flow']
    list_display = ['id', 'label', 'target_flow']


admin.site.register(Status, StatusAdmin)
