from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class AllExercises(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    target_muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE)
    image_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name