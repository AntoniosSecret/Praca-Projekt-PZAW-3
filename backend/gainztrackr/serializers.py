from rest_framework import serializers, generics
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import AllExercises

class AllExercisesSerializer(serializers.ModelSerializer):
    equipment = serializers.StringRelatedField()
    target_muscle = serializers.StringRelatedField()

    class Meta:
        model = AllExercises
        fields = '__all__'

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user