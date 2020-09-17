from django.db import models
from poses.models import StartPose, EndPose


# Create your models here.
class MetaChoreo(models.Model):
    meta_choreo_id = models.CharField(max_length=20)
    url = models.URLField(max_length=150)
    start = models.FloatField()
    end = models.FloatField()

    def __str__(self):
        return self.meta_choreo_id


class Choreo(models.Model):
    choreo_id = models.CharField(max_length=25)
    movement = models.CharField(max_length=130)
    first_start = models.BinaryField(default=0)
    last_end = models.BinaryField(default=0)
    meta_choreo_id = models.ForeignKey(MetaChoreo, on_delete=models.CASCADE)
    start_pose_id = models.ForeignKey(StartPose, on_delete=models.CASCADE)
    end_pose_id = models.ForeignKey(EndPose, on_delete=models.CASCADE)
