from django.db import models


class Team(models.Model):
    name = models.TextField()
    code = models.TextField()
    color_set = models.TextField()

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.TextField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    budget = models.TextField(null=True, blank=True)
    hashtags = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
