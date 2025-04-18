from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    def get(self, request):
        return Response({"message": "This is home"})


class ProfileView(APIView):
    def get(self, request):
        return Response({"message": "This is the profile"})


class AllExercisesView(APIView):
    def get(self, request):
        return Response({"message": "These are all the exercises"})

class LoginView(APIView):
    def get(self, request):
        return Response({"message": "This is the login page"})