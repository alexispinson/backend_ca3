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
        time = timezone.now() + datetime.timedelta(days=30) #30 days in the future
        future_cat = Cat(date_of_birth=time) #create a cat with a date of birth in the future
        self.assertIs(future_cat.is_in_future(), True) #check if the cat is in the future
        #positive test
        time = timezone.now() - datetime.timedelta(days=30) #30 days in the past
        normal_cat = Cat(date_of_birth=time) #create a cat with a date of birth in the past
        self.assertIs(normal_cat.is_in_future(), False) #check if the cat is in the future (should be false obviously)

    def test_too_old_cat(self):
        """
        test_too_old_cat returns False for cats whose date_of_birth
        is too old. (more than 40 years old)
        """
        #negative test
        time = timezone.now() - relativedelta(years=40) #40 years in the past
        too_old_cat = Cat(date_of_birth=time) #create a cat with a date of birth in the past but too much in the past
        self.assertIs(too_old_cat.is_too_old(), True) #check if the cat is too old
        #positive test
        time = timezone.now() - datetime.timedelta(days=30) #30 days in the past
        normal_cat = Cat(date_of_birth=time) #create a cat with a date of birth in the past but not too much this time
        self.assertIs(normal_cat.is_too_old(), False) #check if the cat is too old (should be false obviously)

class UserModelTests(TestCase):
    def test_length_phone_number(self):
        """
        test_length_phone_number returns False if the phone number is not 9 digits long 
        """
        #negative test
        phone_number = 879896776456868 #try with a phone number that is too long
        user = User(phone_number=phone_number) #create a user with this phone number
        self.assertIs(user.phone_number_length(), False) #check if the phone number is 9 digits long
        #positive test
        phone_number = 879896776 #try with a phone number that is 9 digits long
        user = User(phone_number=phone_number) #create a user with this phone number
        self.assertIs(user.phone_number_length(), True) #check if the phone number is 9 digits long (obviously it should be true)
    def test_email_valid(self):
        """
        test_email_valid returns False if the email doesn't contain an @
        """
        #negative test
        email = "testemail.com" #try with an email that doesn't contain an @
        user = User(email=email) #create a user with this email
        self.assertIs(user.countains_at(), False) #check if the email contains an @
        #positive test
        email = "alexispinson78@gmail.com" #try with an email that contains an @
        user = User(email=email) #create a user with this email
        self.assertIs(user.countains_at(), True) #check if the email contains an @ (obviously it should be true)
    def test_len_password(self):
        """
        test_len_password return False if the password is too short
        """
        #negative test
        password = "1" #try with a password that is too short
        user = User(password=password) #create a user with this password
        self.assertIs(user.good_len_password(), False) #check if the password is too short
        #positive test
        password="smklfjsdfmqsjk" #try with a password that is long enough
        user = User(password=password) #create a user with this password
        self.assertIs(user.good_len_password(), True) #check if the password is too short (obviously it should be true)
    def test_maj_password(self):
        """
        test_maj_password return False if the password doesn't contain a capital letter
        """
        #negative test
        password = "1" #try with a password that doesn't contain a capital letter
        user = User(password=password) #create a user with this password
        self.assertIs(user.is_maj(), False) #check if the password contains a capital letter
        #positive test
        password = "Smklfjsdfmqsjk" #try with a password that contains a capital letter
        user = User(password=password) #create a user with this password
        self.assertIs(user.is_maj(), True) #check if the password contains a capital letter (obviously it should be true)
    def test_number_password(self):
        """
        test_number_password return False if the password doesn't contain a number
        """
        #negative test
        password = "Smklfjsdfmqsjk" #try with a password that doesn't contain a number
        user = User(password=password) #create a user with this password
        self.assertIs(user.is_number(), False) #check if the password contains a number
        #positive test
        password = "6klmjqsklf" #try with a password that contains a number
        user = User(password=password) #create a user with this password
        self.assertIs(user.is_number(), True) #check if the password contains a number (obviously it should be true)
