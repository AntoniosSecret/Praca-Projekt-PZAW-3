from rest_framework import serializers
from .models import AllExercises

class AllExercisesSerializer(serializers.ModelSerializer):
    equipment = serializers.StringRelatedField()
    target_muscle = serializers.StringRelatedField()

    class Meta:
        model = AllExercises
        fields = '__all__'
