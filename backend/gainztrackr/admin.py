from django.contrib import admin
from django.contrib.auth.models import Group
from .models import AllExercises, Muscle, Category, Equipment

admin.site.unregister(Group)

admin.site.register(AllExercises)
admin.site.register(Muscle)
admin.site.register(Category)
admin.site.register(Equipment)