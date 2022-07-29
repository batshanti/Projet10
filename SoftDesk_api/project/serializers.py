from rest_framework.serializers import ModelSerializer
from project.models import Projects


class ProjectsSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = ["title", "description", "type"]

    def create(self, validated_data):
        project = Projects(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
        )
        project.save()

        return project
