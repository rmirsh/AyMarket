from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from aymarket.core.views import index, contact

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
