# Import necessary modules for testing
from django.test import TestCase
from django.urls import reverse

# Import Cat and User models from the application's models module
from ..models import Cat, User

# Define a test class for views related to cats
class CatViewTests(TestCase):
    # Test the connection view
    def test_connection(self):
        # Get the response from the connection view using the reverse function
        response = User.objects.get(reverse('cat:connection'))
        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response contains the string "Connection"
        self.assertContains(response, "Connection")
        # Check that the template used to render the response is 'user/connection.html'
        self.assertTemplateUsed(response, 'user/connection.html')
        
    # Test the sign-in view
    def test_signin(self):
        # Get the response from the sign-in view using the reverse function
        response = User.objects.get(reverse('cat:signin'))
        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response contains the string "Sign in"
        self.assertContains(response, "Sign in")
        # Check that the template used to render the response is 'user/signin.html'
        self.assertTemplateUsed(response, 'user/signin.html')
        
    # Test the detail view
    def test_detail(self):
        # Create a test user and cat
        user = User.objects.create(name="test", password="test")
        cat = Cat.objects.create(name="test", date_of_birth="2019-01-01", user=user)
        # Get the response from the detail view using the reverse function and passing the user and cat ids as arguments
        response = User.objects.get(reverse('cat:detail', args=[user.id, cat.id]))
        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response contains the string "Details"
        self.assertContains(response, "Details")
        # Check that the template used to render the response is 'cat/detail.html'
        self.assertTemplateUsed(response, 'cat/detail.html')
        
    # Test the user detail view
    def test_udetail(self):
        # Create a test user
        user = User.objects.create(name="test", password="test")
        # Get the response from the user detail view using the reverse function and passing the user id as an argument
        response = User.objects.get(reverse('cat:udetail', args=[user.id]))
        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response contains the string "Details"
        self.assertContains(response, "Details")
        # Check that the template used to render the response is 'user/udetail.html'
        self.assertTemplateUsed(response, 'user/udetail.html')
        
    def test_add(self):
        # Create a test user
        user = User.objects.create(name="test", password="test")
        # Get the response from the add view using the reverse function to generate the URL
        response = User.objects.get(reverse('cat:add', args=[user.id]))
        # Ensure the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Ensure that the response contains the text "Add"
        self.assertContains(response, "Add")
        # Ensure that the add.html template is used
        self.assertTemplateUsed(response, 'cat/add.html')

    def test_delete(self):
        # Create a test user
        user = User.objects.create(name="test", password="test")
        # Create a test cat belonging to the test user
        cat = Cat.objects.create(name="test", date_of_birth="2019-01-01", user=user)
        # Get the response from the delete view using the reverse function to generate the URL
        response = User.objects.get(reverse('cat:delete', args=[user.id, cat.id]))
        # Ensure the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Ensure that the response contains the text "Delete"
        self.assertContains(response, "Delete")
        # Ensure that the delete.html template is used
        self.assertTemplateUsed(response, 'cat/delete.html')