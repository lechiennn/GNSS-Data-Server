from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from process.models import *
from process.serializers import *

# Create your views here.


class StationViewSet(ListModelMixin,
                     CreateModelMixin,
                     GenericViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class DataViewSet(ListModelMixin, GenericViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
