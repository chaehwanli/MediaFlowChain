from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

class Scene(models.Model):
    movie = models.ForeignKey(Movie, related_name="scenes", on_delete=models.CASCADE)
    scene_number = models.IntegerField()
    description = models.TextField()

class Character(models.Model):
    name = models.CharField(max_length=100)
    personality = models.TextField()
    background = models.TextField()
    scenes = models.ManyToManyField(Scene, related_name="characters")

class Script(models.Model):
    scene = models.ForeignKey(Scene, related_name="scripts", on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

class Music(models.Model):
    scene = models.ForeignKey(Scene, related_name="music", on_delete=models.CASCADE)
    file_path = models.FileField(upload_to="music/")
    type = models.CharField(max_length=50)
