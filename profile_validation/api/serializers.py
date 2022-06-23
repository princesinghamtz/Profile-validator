from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Duplicate_profile


# Order place
class Duplicate_profileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Duplicate_profile
        fields = ['profile1', 'profile2', 'total_match_score', 'matching_attributes',
                  'non_matching_attributes', 'ignored_attributes']
