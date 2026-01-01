from django.urls import include
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('manager/', include('manager.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
