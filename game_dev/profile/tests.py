"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User

#FIXME need to namespace everything correctly should be:
#from game_dev.profile.models import Profile
from profile.models import Profile


class ProfileTestCase(TestCase):
    def test_simple(self):
        user = User.objects.create()
        profile = Profile.objects.create(user=user)
        self.assertEqual(user.profile, profile)
