from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

""" Test fonksiyonları test ile başlamak zorunda
    Django bu şekilde test ediyor"""

def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@aydogan.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        """ Şifre şifrelenmiş olduğu için (encripted) check pasword
        metoduyla kontrol edilmeli"""

    def test_new_user_email_normalized(self):
	       """Test the email for a new user is normalized"""
	       email = 'test@AYDOGAN.com'
	       user = get_user_model().objects.create_user(email, 'test123')

	       self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
            )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
            )

        self.assertEqual(str(tag), tag.name)
