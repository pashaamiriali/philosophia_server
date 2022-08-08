from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class RoomModel(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OwnershipModel(models.Model):
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_primary = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DebateModel(models.Model):
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ParticipationModel(models.Model):
    debate = models.ForeignKey(DebateModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReferenceModel(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ThoughtModel(models.Model):
    participation = models.ForeignKey(ParticipationModel, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField()
    reference = models.ForeignKey(ReferenceModel, on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ObservationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    thought = models.ForeignKey(ThoughtModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OpinionModel(models.Model):
    observation = models.ForeignKey(ObservationModel, on_delete=models.CASCADE)
    content = models.TextField()
    is_positive = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
