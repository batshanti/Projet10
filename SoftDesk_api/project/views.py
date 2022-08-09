from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from project.serializers import ProjectsSerializer
from project.models import Projects


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        if not user.is_anonymous:
            return Projects.objects.filter(author=user)

        return Projects.objects.none()
