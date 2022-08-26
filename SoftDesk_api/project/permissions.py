from rest_framework.permissions import BasePermission, SAFE_METHODS
from project.models import Projects, Contributors, Issues, Comments


class ProjectPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.author
        else:
            return False


class ContributorPermission(BasePermission):

    def has_permission(self, request, view):

        contributors = Contributors.objects.filter(
            projet_id=view.kwargs['projects_pk']
        )

        for Contributor in contributors:
            if Contributor.user_id == request.user:
                return True
            else:
                return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:

            project = Projects.objects.get(id=view.kwargs['projects_pk'])

            return request.user == project.author
        return False


class IssuePermission(BasePermission):

    def has_permission(self, request, view):

        contributors = Contributors.objects.filter(
            projet_id=view.kwargs['projects_pk']
        )
        contributor_ids = []
        for Contributor in contributors:
            contributor_ids.append(Contributor.user_id)
        if request.user in contributor_ids:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:

            return request.user == obj.author_user_id
        return False


class CommentPermission:

    def has_permission(self, request, view):

        contributors = Contributors.objects.filter(
            projet_id=view.kwargs['projects_pk']
        )
        contributor_ids = []
        for Contributor in contributors:
            contributor_ids.append(Contributor.user_id)
        print(contributor_ids)
        if request.user in contributor_ids:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        if request.method in ['PUT', 'PATCH', 'DELETE']:

            return request.user == obj.author_user_id
        return False
