from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AllExercises
from .serializers import AllExercisesSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics


class HomeView(APIView):    
    def get(self, request):
        return Response({"message": "This is home"})


class ProfileView(APIView):
    def get(self, request):
        return Response({"message": "This is the profile"})


class AllExercisesView(APIView):
    def get(self, request):
        exercises = AllExercises.objects.select_related('equipment', 'target_muscle')
        return Response(AllExercisesSerializer(exercises, many=True).data)

class LoginView(APIView):
    def get(self, request):
        return Response({"message": "This is the login page"})

class ExerciseView(APIView):
    def get(self, request, id):
        try:
            exercise = AllExercises.objects.get(id=id)
            serializer = AllExercisesSerializer(exercise)
            return Response(serializer.data)
        except AllExercises.DoesNotExist:
            return Response({"error": "Exercise not found"}, status=404)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer