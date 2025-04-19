from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('all-exercises/', views.AllExercisesView.as_view(), name='all-exercises'),
    path('exercise/<int:id>', views.ExerciseView.as_view(), name='exercises'),
    path('login/', views.LoginView.as_view(), name='login'),
]