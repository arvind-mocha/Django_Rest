from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    # setUp is the function ran before every tests
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='ddkkzz996@gmail.com', password='test123')

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='safiazzzx@gmail.com', password='test123', name='username')

    def test_users_listed(self):
        # testing weather users are listed on the user page

        url = reverse('admin:core_user_changelist')  # gets current url
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

        def test_user_change_page(self):
            # testing wearther the use edit page works
            url = reverse('admin:core_user_change', args=[self.user.id])  # gets current url
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)

        def test_create_user_page(self):
            # test that the create user page works
            url = reverse('admin:core_user_add', args=[self.user.id])  # gets current url
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
