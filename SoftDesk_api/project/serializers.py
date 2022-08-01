from rest_framework.serializers import ModelSerializer
from project.models import Projects


class ProjectsSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = ["title", "description", "type", "author"]


