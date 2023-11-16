from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from decouple import config
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = config('SITE_NAME')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_register.urls')),
]
urlpatterns += i18n_patterns(
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('application/', include('application.urls', namespace='application')),
    path('ui/', include('ui.urls', namespace='ui')),
    path('feature/', include('feature.urls', namespace='feature')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
