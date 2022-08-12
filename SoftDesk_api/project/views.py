from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from project.serializers import ProjectsSerializer, ProjectsDetailSerializer, ContributorsSerializer, UserSerializer, IssueslSerializer
from project.models import Projects, Contributors, Issues


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer
    detail_serializer_class = ProjectsDetailSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Projects.objects.filter(author=user)

        return Projects.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorsViewset(ModelViewSet):
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = ContributorsSerializer
            return self.serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        contributors_project = Contributors.objects.filter(projet_id=self.kwargs['projects_pk'])
        user_ids = []
        for Contributor in contributors_project:
            user_ids.append(Contributor.user_id.id)

        return User.objects.filter(id__in=user_ids)

    def get_serializer_context(self):
        context = super(ContributorsViewset, self).get_serializer_context()
        project = Projects.objects.get(pk=self.kwargs['projects_pk'])
        context.update({"project_id": project})
        return context


class IssuesViewset(ModelViewSet):
    serializer_class = IssueslSerializer

    def get_queryset(self):
        return Issues.objects.filter(project_id=self.kwargs['projects_pk'])

    def get_serializer_context(self):
        context = super(IssuesViewset, self).get_serializer_context()
        project = Projects.objects.get(pk=self.kwargs['projects_pk'])
        context.update({"project_id": project})
        return context
