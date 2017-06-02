from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250)
    upvote = models.IntegerField(max_length=250, null=True, blank=True)
    downvote = models.IntegerField(max_length=250, null=True, blank=True)