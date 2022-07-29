from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from project.serializers import ProjectsSerializer
from project.models import Projects


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Projects.objects.all()
