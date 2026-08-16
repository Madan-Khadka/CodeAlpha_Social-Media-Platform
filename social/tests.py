from django.test import TestCase
from django.contrib.auth.models import User

from .models import (
    Follow,
    Like,
    Post,
)


class SocialHubModelTests(TestCase):

    def setUp(self):

        self.user1 = User.objects.create_user(
            username="user1",
            password="password123",
        )

        self.user2 = User.objects.create_user(
            username="user2",
            password="password123",
        )


    def test_post_creation(self):

        post = Post.objects.create(
            author=self.user1,
            content="Hello SocialHub!",
        )

        self.assertEqual(
            post.author,
            self.user1,
        )


    def test_like_creation(self):

        post = Post.objects.create(
            author=self.user1,
            content="Test post",
        )

        Like.objects.create(
            user=self.user2,
            post=post,
        )

        self.assertEqual(
            post.likes.count(),
            1,
        )


    def test_follow_creation(self):

        Follow.objects.create(
            follower=self.user1,
            following=self.user2,
        )

        self.assertEqual(
            Follow.objects.count(),
            1,
        )