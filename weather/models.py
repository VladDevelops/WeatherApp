from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)

    def srt__(self):
        return self.name
