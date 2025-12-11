# shaikh_portfolio/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # include the core app for the root path - this makes '/' be handled by core.urls
    path('', include('core.urls')),

    # (Optionally) any other top-level includes go here
]

# Serve MEDIA files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
