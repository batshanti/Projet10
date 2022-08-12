from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from project.models import Projects, Contributors, Issues


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ProjectsSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = ["id", "title", "description", "type"]

    def create(self, validated_data):
        project = Projects(
            title=validated_data['title'],
            description=validated_data['description'],
            type=validated_data['type'],
            author=self.context['request'].user
        )
        project.save()
        pjt = Projects.objects.get(id=project.id)
        contributor = Contributors(
            permission='all',
            role='author',
            projet_id=pjt,
            user_id=self.context['request'].user
        )
        contributor.save()
        return project


class ProjectsDetailSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type']


class ContributorsSerializer(ModelSerializer):

    class Meta:
        model = Contributors
        fields = ['id', 'permission', 'role', 'user_id']


class IssueslSerializer(ModelSerializer):

    class Meta:
        model = Issues
        fields = [
            'title',
            'description',
            'tag',
            'priority',
            'created_time',
            'status',
            'project_id',
            'author_user_id',
            'assignee_user_id'
        ]
