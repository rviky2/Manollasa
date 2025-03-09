from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('university/<str:template_name>',
         UniversityTemplateView.as_view(), name='university view'),
    path('consultancy/<str:template_name>',
         ConsultancyTemplateView.as_view(), name='Consultancy view'),
    path('freeservice/<str:template_name>',
         FreeServiceTemplateView.as_view(), name='Consultancy view'),
    path('<str:something>', PageNotFound, name='PageNotFound')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
