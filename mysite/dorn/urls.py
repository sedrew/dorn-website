from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', post_list)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)