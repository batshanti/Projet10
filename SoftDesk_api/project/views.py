from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from project.serializers import (
    ProjectsSerializer,
    ProjectsDetailSerializer,
    ContributorsSerializer,
    UserSerializer,
    IssueslSerializer,
    CommentsSerializer,
    IssuesDetailSerializer
)
from project.permissions import (
    ProjectPermission,
    IssuePermission,
    ContributorPermission,
    CommentPermission
)
from project.models import Projects, Contributors, Issues, Comments


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer
    detail_serializer_class = ProjectsDetailSerializer
    permission_classes = [IsAuthenticated, ProjectPermission]

    def get_queryset(self):
        user = self.request.user
        user_contributor = Contributors.objects.filter(user_id=user)
        project_ids = []

        for contrib in user_contributor:
            project_ids.append(contrib.projet_id.id)

        return Projects.objects.filter(id__in=project_ids)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated, ContributorPermission]

    def get_queryset(self):
        return Contributors.objects.filter(
            projet_id=self.kwargs['projects_pk']
        )

    def perform_create(self, serializer):
        project = Projects.objects.get(id=self.kwargs['projects_pk'])
        serializer.save(projet_id=project)


class IssuesViewset(ModelViewSet):
    serializer_class = IssueslSerializer
    detail_serializer_class = IssuesDetailSerializer
    permission_classes = [IsAuthenticated, IssuePermission]

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
    permission_classes = [IsAuthenticated, CommentPermission]

    def get_queryset(self):
        return Comments.objects.filter(issue_id=self.kwargs['issues_pk'])

    def perform_create(self, serializer):
        issue = Issues.objects.get(id=self.kwargs['issues_pk'])
        serializer.save(issue_id=issue, author_user_id=self.request.user)
