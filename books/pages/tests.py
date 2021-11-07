from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView
# Create your tests here.
class HomePageTest(SimpleTestCase):
    
    def setup(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def rest_home_page_status_code(self):
        response = self.client.get('/')
        self.asserRqual(response.status_code, 200)
        
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Homepage')
        
    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.'
        )
        
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )