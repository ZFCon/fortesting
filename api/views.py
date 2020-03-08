from django.http import HttpResponse

from django.contrib.auth.models import User

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return Response('hi')

def four_test(request, gg):
    return HttpResponse(gg)