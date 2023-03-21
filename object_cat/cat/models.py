# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta
#This class is for all the differents cats that you want to give
class Cat(models.Model):
    catid = models.AutoField(db_column='catID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    treatment = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    userid = models.ForeignKey('User', models.CASCADE, db_column='userID')  # Field name made lowercase.

    def is_in_future(self):
        return self.date_of_birth >= timezone.now()
    def is_too_old(self):
        return self.date_of_birth <= timezone.now() - relativedelta(years=40)
    class Meta:
        managed = False
        db_table = 'cat'

#This class if for the users (for this first project, I didn't use the django user model)
class User(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
    
    def phone_number_length(self):
        return len(str(self.phone_number)) == 9
    def countains_at(self):
        return "@" in self.email
    def good_len_password(self):
        return len(self.password) >= 8
    def is_maj(self):
        return any(char.isupper() for char in self.password)
    def is_number(self):
        return any(char.isdigit() for char in self.password)
