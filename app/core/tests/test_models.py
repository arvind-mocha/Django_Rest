from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        # Testing weather creating a new user with an email is successful

        email = 'ddkkzz996@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))  # we can't use assert equal for password because password is encrypted

    def test_new_user_normalized(self):
        # testing weather the users email is valid. we are only checking weather the email is in lowercase on this test
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # testing email field is entered by the user

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')  # test passes when value error is raised if user doesn't give email

    def test_create_new_superuser(self):
        # testing creating a new superuser
        user = get_user_model().objects.create_superuser('ddkkzz996@gmail.com', 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
