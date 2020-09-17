from django.db import models
from abc import *


# Create your models here.

class Pose(models.Model):
    pose_id = models.CharField(max_length=30)
    type = models.IntegerField()
    x_mean = models.FloatField()
    y_min = models.FloatField()
    y_max = models.FloatField()

    class Meta:
        abstract = True


class StartPose(Pose):
    pass


class EndPose(Pose):
    pass
