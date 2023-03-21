import datetime

from django.test import TestCase
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from cat.models import User, Cat

class CatModelTests(TestCase):
    def test_future_cat(self):
        """
        test_future_cat returns False for cats whose date_of_birth
        is in the future.
        """
        #negative test
        time = timezone.now() + datetime.timedelta(days=30)
        future_cat = Cat(date_of_birth=time)
        self.assertIs(future_cat.is_in_future(), True)
        #positive test
        time = timezone.now() - datetime.timedelta(days=30)
        normal_cat = Cat(date_of_birth=time)
        self.assertIs(normal_cat.is_in_future(), False)

    def test_too_old_cat(self):
        """
        test_too_old_cat returns False for cats whose date_of_birth
        is too old. (more than 40 years old)
        """
        #negative test
        time = timezone.now() - relativedelta(years=40)
        too_old_cat = Cat(date_of_birth=time)
        self.assertIs(too_old_cat.is_too_old(), True)
        #positive test
        time = timezone.now() - datetime.timedelta(days=30)
        normal_cat = Cat(date_of_birth=time)
        self.assertIs(normal_cat.is_too_old(), False)

class UserModelTests(TestCase):
    def test_length_phone_number(self):
        """
        test_length_phone_number returns False if the phone number is not 9 digits long 
        """
        #negative test
        phone_number = 879896776456868
        user = User(phone_number=phone_number)
        self.assertIs(user.phone_number_length(), False)
        #positive test
        phone_number = 879896776
        user = User(phone_number=phone_number)
        self.assertIs(user.phone_number_length(), True)
    def test_email_valid(self):
        """
        test_email_valid returns False if the email doesn't contain an @
        """
        #negative test
        email = "testemail.com"
        user = User(email=email)
        self.assertIs(user.countains_at(), False)
        #positive test
        email = "alexispinson78@gmail.com"
        user = User(email=email)
        self.assertIs(user.countains_at(), True)
    def test_len_password(self):
        """
        test_len_password return False if the password is too short
        """
        #negative test
        password = "1"
        user = User(password=password)
        self.assertIs(user.good_len_password(), False)
        #positive test
        password="smklfjsdfmqsjk"
        user = User(password=password)
        self.assertIs(user.good_len_password(), True)
    def test_maj_password(self):
        """
        test_maj_password return False if the password doesn't contain a capital letter
        """
        #negative test
        password = "1"
        user = User(password=password)
        self.assertIs(user.is_maj(), False)
        #positive test
        password = "Smklfjsdfmqsjk"
        user = User(password=password)
        self.assertIs(user.is_maj(), True)
    def test_number_password(self):
        """
        test_number_password return False if the password doesn't contain a number
        """
        #negative test
        password = "Smklfjsdfmqsjk"
        user = User(password=password)
        self.assertIs(user.is_number(), False)
        #positive test
        password = "6klmjqsklf"
        user = User(password=password)
        self.assertIs(user.is_number(), True)
