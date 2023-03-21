#test the differents urls
# Compare this snippet from cat/tests/test-urls.py:
from django.urls import path

from cat import views

app_name = 'cat'
urlpatterns = [
    path('', views.connection, name='connection'),#This is the first page
    path('signin/', views.signin, name='signin'),#This is the page where you can sign in
    path('user/<int:user_id>/<int:cat_id>/', views.detail, name='detail'),#This is the page where you can see the details of a cat
    path('user/<int:user_id>/', views.udetail, name='udetail'),#This is the page where you can see the details of a user
    path('user/<int:user_id>/add', views.add, name="add"),#This is the page where you can add a cat
    path('user/<int:user_id>/delete/<int:id>', views.delete, name='delete'),#This is the page where you can delete a cat
    path('user/<int:user_id>/edit/<int:cat_id>', views.edit, name='edit'),#This is the page where you can edit a cat
    path('user/<int:user_id>/delete',views.udelete, name = 'udelete'),#This is the page where you can delete a user
    path('user/<int:user_id>/edit', views.uedit, name='uedit'),#This is the page where you can edit a user
    path('user/<int:user_id>/changepassword',views.change_password,name="change_password"),#page to change the password
]
#test the differents urls
# Compare this snippet from cat/tests/test-urls.py:
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cat.views import connection, signin, detail, udetail, add, delete, edit, udelete, uedit, change_password

class TestUrls(SimpleTestCase):
    def test_connection_url_is_resolved(self):
        url = reverse('cat:connection')
        self.assertEquals(resolve(url).func, connection)

    def test_signin_url_is_resolved(self):
        url = reverse('cat:signin')
        self.assertEquals(resolve(url).func, signin)

    def test_detail_url_is_resolved(self):
        url = reverse('cat:detail', args=[1,1])
        self.assertEquals(resolve(url).func, detail)

    def test_udetail_url_is_resolved(self):
        url = reverse('cat:udetail', args=[1])
        self.assertEquals(resolve(url).func, udetail)

    def test_add_url_is_resolved(self):
        url = reverse('cat:add', args=[1])
        self.assertEquals(resolve(url).func, add)

    def test_delete_url_is_resolved(self):
        url = reverse('cat:delete', args=[1,1])
        self.assertEquals(resolve(url).func, delete)

    def test_edit_url_is_resolved(self):
        url = reverse('cat:edit', args=[1,1])
        self.assertEquals(resolve(url).func, edit)

    def test_udelete_url_is_resolved(self):
        url = reverse('cat:udelete', args=[1])
        self.assertEquals(resolve(url).func, udelete)

    def test_uedit_url_is_resolved(self):
        url = reverse('cat:uedit', args=[1])
        self.assertEquals(resolve(url).func, uedit)

    def test_change_password_url_is_resolved(self):
        url = reverse('cat:change_password', args=[1])
        self.assertEquals(resolve(url).func, change_password)