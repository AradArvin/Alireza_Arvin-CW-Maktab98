from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Author

# Create your tests here.


class AuthorTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.author = Author.objects.create(
            profile_image="../media/author/images.jpeg",
            name=cls.user.username,
            bio="test bio",
        )

    def test_author_model(self):
        self.assertEqual(self.author.profile_image, "../media/author/images.jpeg")
        self.assertEqual(self.author.name, "testuser")
        self.assertEqual(str(self.author), "testuser")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/author/1/")
        self.assertEqual(response.status_code, 200)

    def test_author_listview(self):
        response = self.client.get(reverse("author"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
        self.assertTemplateUsed(response, "author.html")

    def test_author_detailview(self):
        response = self.client.get(
            reverse("author_detail", kwargs={"pk": self.author.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test bio")
        self.assertTemplateUsed(response, "author_detail.html")
