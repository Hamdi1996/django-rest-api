from django.test import TestCase
from django.utils import timezone
from .models import UserProfile, ProfileFeedItem

class UserProfileTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_profile = UserProfile.objects.create(
            email="admin@example.com",
            name="admin",
            is_active=True,
            is_staff=True
        )

    def test_user_profiles_fields(self):
        self.assertIsInstance(self.user_profile.email, str)
        self.assertIsInstance(self.user_profile.name, str)
        self.assertIsInstance(self.user_profile.is_active, bool)
        self.assertIsInstance(self.user_profile.is_staff, bool)

class ProfileFeedItemTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_profile = UserProfile.objects.create(
            email="user@example.com",
            name="user",
            is_active=True,
            is_staff=False
        )
        cls.feed = ProfileFeedItem.objects.create(
            user_profile=user_profile,
            status_text="active",
            created_on=timezone.now()  # Use timezone.now() to create a timezone-aware datetime object
        )

    def test_feed_fields(self):
        self.assertIsInstance(self.feed.status_text, str)
        self.assertIsInstance(self.feed.created_on, timezone.datetime)
