from django.urls import path, include, register_converter

from rest_framework import routers

from . import views

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

register_converter(FourDigitYearConverter, 'haha')


route = routers.DefaultRouter()
route.register('userview', views.UserViewSet, basename='userviewset')

urlpatterns = [
    path('', include(route.urls)),
    path('four/<haha:gg>', views.four_test),
]
