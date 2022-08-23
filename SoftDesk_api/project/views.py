from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from project.serializers import (
    ProjectsSerializer,
    ProjectsDetailSerializer,
    ContributorsSerializer,
    UserSerializer,
    IssueslSerializer,
    CommentsSerializer,
    IssuesDetailSerializer
)

from project.models import Projects, Contributors, Issues, Comments


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer
    detail_serializer_class = ProjectsDetailSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            user_contributor = Contributors.objects.filter(user_id=user)
            project_ids = []
            for contrib in user_contributor:
                project_ids.append(contrib.projet_id.id)
            return Projects.objects.filter(id__in=project_ids)

        return Projects.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorsSerializer

    def get_queryset(self):
        return Contributors.objects.filter(
            projet_id=self.kwargs['projects_pk']
        )


class IssuesViewset(ModelViewSet):
    serializer_class = IssueslSerializer
    detail_serializer_class = IssuesDetailSerializer

    def get_queryset(self):
        return Issues.objects.filter(project_id=self.kwargs['projects_pk'])

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super(IssuesViewset, self).get_serializer_context()
        user = User.objects.get(username=self.request.user)
        project = Projects.objects.get(id=self.kwargs['projects_pk'])
        context.update({'project_id': project, 'author_user_id': user})
        return context


class CommentsViewset(ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.filter(issue_id=self.kwargs['issues_pk'])






        # contributors_project = Contributors.objects.filter(projet_id=self.kwargs['projects_pk'])
        # user_ids = []
        # for Contributor in contributors_project:
        #     user_ids.append(Contributor.user_id.id)

        # return User.objects.filter(id__in=user_ids)