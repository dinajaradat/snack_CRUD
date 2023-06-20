from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack


class SnackPageTests(TestCase):
    def setUp(self):
        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a snack object for testing
        self.snack = Snack.objects.create(
            title ='Test Snack',
            purchaser = self.user,
            description ='Test snack description'
        )

    def test_snack_list_page(self):
        # Generate the URL for the snack list page
        url = reverse('snacks')

        # Make a GET request to the URL
        response = self.client.get(url)

        # Verify the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify the template used is 'snack_list.html'
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_page(self):
        # Generate the URL for the snack detail page using the snack's ID
        url = reverse('snack_detail', args=[self.snack.pk])

        # Make a GET request to the URL
        response = self.client.get(url)

        # Verify the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify the template used is 'snack_detail.html'
        self.assertTemplateUsed(response, 'snack_detail.html')

        # Verify the content of the response
        self.assertContains(response, self.snack.title)
        self.assertContains(response, self.snack.description)
        self.assertContains(response, self.snack.purchaser.username)

    def test_str_method(self):
        self.assertEqual(str(self.snack), "Test Snack")

    def test_create_view(self):
            obj = {
                'title': "Test Snack 2",
                'description': 'Test snack description 2',
                'purchaser': self.user.id,
            }

            url = reverse('snack_create')
            response = self.client.post(path=url, data=obj, follow=True)
            self.assertRedirects(response, reverse('snacks'))

    def test_delete_view(self):
            obj = {
                'title': "Test Snack 2",
                'description': 'Test snack description 2',
                'purchaser': self.user.id,
            }

            url = reverse('snack_delete', args=[self.user.id])
            response = self.client.post(path=url, data=obj, follow=True)
            self.assertRedirects(response, reverse('snacks'))

    def test_update_view(self):
        updated_obj = {
            'title': "Updated Snack",
            'description': 'Updated snack description',
            'purchaser': self.user.id,
        }

        url = reverse('snack_update', args=[self.snack.pk])
        response = self.client.post(path=url, data=updated_obj, follow=True)
        self.assertRedirects(response, reverse('snacks'))
        self.snack.refresh_from_db()  # Refresh the object from the database
        self.assertEqual(self.snack.title, updated_obj['title'])
        self.assertEqual(self.snack.description, updated_obj['description'])
        self.assertEqual(self.snack.purchaser, self.user)

