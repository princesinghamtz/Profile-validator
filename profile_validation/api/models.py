from django.db import models

# Create your models here.
class Duplicate_profile(models.Model):
    profile1 = models.CharField(max_length=100)
    profile2 = models.CharField(max_length=100)
    total_match_score = models.IntegerField()
    matching_attributes = models.TextField(blank=True)
    non_matching_attributes = models.TextField(blank=True)
    ignored_attributes = models.TextField(blank=True)

    def __str__(self):
        return self.profile1 + '|' + self.profile2