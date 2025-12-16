from django.db import models

# These are placeholder models for admin and DRF compatibility, as data is stored in MongoDB collections directly.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=50)
    members = models.JSONField()
    class Meta:
        managed = False
        db_table = 'teams'

class Activity(models.Model):
    user_email = models.EmailField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'workouts'
