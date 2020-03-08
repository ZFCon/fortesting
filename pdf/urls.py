from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.pdf_view),
    path('django_html', views.detail_to_pdf)
]
