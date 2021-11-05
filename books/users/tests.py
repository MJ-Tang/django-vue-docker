from django.test import TestCase
from django.contrib.auth import  get_user_model

# Create your tests here.

class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'michael',
            email = 'michael@email.com',
            password = 'Tangmj23'
        )
        
        self.assertEqual(user.username, 'michael')
        self.assertEqual(user.email, 'michael@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'superadmin',
            email = 'superadmin@email.com',
            password = 'superadmin123'
        )
        
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)