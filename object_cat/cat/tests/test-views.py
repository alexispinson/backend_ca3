#testing views with reverse
from django.test import TestCase
from django.urls import reverse

from ..models import Cat, User

class CatViewTests(TestCase):
    def test_connection(self):
        """
        test_connection returns the connection page
        """
        response = User.objects.get(reverse('cat:connection'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Connection")
        self.assertTemplateUsed(response, 'user/connection.html')
    def test_signin(self):
        """
        test_signin returns the signin page
        """
        response = User.objects.get(reverse('cat:signin'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in")
        self.assertTemplateUsed(response, 'user/signin.html')
    def test_detail(self):
        """
        test_detail returns the detail page
        """
        user = User.objects.create(name="test", password="test")
        cat = Cat.objects.create(name="test", date_of_birth="2019-01-01", user=user)
        response = User.objects.get(reverse('cat:detail', args=[user.id, cat.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Details")
        self.assertTemplateUsed(response, 'cat/detail.html')
    def test_udetail(self):
        """
        test_udetail returns the udetail page
        """
        user = User.objects.create(name="test", password="test")
        response = User.objects.get(reverse('cat:udetail', args=[user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Details")
        self.assertTemplateUsed(response, 'user/udetail.html')
    def test_add(self):
        """
        test_add returns the add page
        """
        user = User.objects.create(name="test", password="test")
        response = User.objects.get(reverse('cat:add', args=[user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add")
        self.assertTemplateUsed(response, 'cat/add.html')
    def test_delete(self):
        """
        test_delete returns the delete page
        """
        user = User.objects.create(name="test", password="test")
        cat = Cat.objects.create(name="test", date_of_birth="2019-01-01", user=user)
        response = User.objects.get(reverse('cat:delete', args=[user.id, cat.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete")
        self.assertTemplateUsed(response, 'cat/delete.html')