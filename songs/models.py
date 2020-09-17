from django.db import models

# Create your models here.
class MetaSong(models.Model):
    meta_song_id = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    duration = models.FloatField()

    def __str__(self):
        return self.id


class Song(models.Model):
    song_id = models.CharField(primary_key=True, max_length=25)
    bpm = models.FloatField()
    meta_song_id = models.ForeignKey(MetaSong, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_id
