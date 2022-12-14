from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class SignupSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [

            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        ]

    def validate(self, data):
        if data['password'] != data['password2']:

            raise serializers.ValidationError(
                'password and password2 are different'
            )
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


