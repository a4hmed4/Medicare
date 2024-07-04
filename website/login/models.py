from django.db import models
from datetime import date, datetime, timezone
from importlib.abc import PathEntryFinder
from django import forms
from django.db import models
from django.forms import TextInput, Textarea, ValidationError
#from phonenumbers import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
from django.core.exceptions import ValidationError


class signup(models.Model):
        first_name = models.CharField(max_length=60, default='')
        last_name = models.CharField(max_length=50, default='')
        date_of_birth = models.DateField(default=date.today)
        age = models.IntegerField(null=True, blank=True)
        Gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
         ]
        Gender = models.CharField(max_length=6, choices=Gender, default='')
        photo = models.FileField(upload_to='ID/%y/%m/%d', default='')
        phone_number =  models.CharField(max_length=20, default='')
        email = models.EmailField(default='')
        height = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
        weight = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])

       #--------Blood type------------
        BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
         ]
        blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, default='')

        Chronic_Diseases =[
       ('Yes', 'Yes'),
       ('No', 'No')
         ]
        Chronic_Diseases = models.CharField(max_length=3, choices=Chronic_Diseases, default='')
       
        allergies = [
       ('Yes', 'Yes'),
       ('No', 'No')
         ]
        allergies = models.CharField(max_length=3, choices=allergies, default='')

        Diagnosis =  models.CharField(max_length=100, default='')
       #--------
        street = models.CharField(max_length=100, default='')
        city = models.CharField(max_length=100, default='')
        state = models.CharField(max_length=100, default='')
        country = models.CharField(max_length=100, default='')

        perform_a_surgery_or_a_medical_examination = models.BooleanField(default=True)
        registered_with_an_insurance_company = models.BooleanField(default=True)
        If_you_are_registered_what_is_the_insurance_company =  models.CharField(max_length=50,null=True, blank=True, default='')
        If_you_are_registered_what_is_the_policy_number  =  models.CharField(max_length=20,null=True, blank=True, default='')
        name_of_an_emergency_contact = models.CharField(max_length=50, default='')
        phone_for_emergency_medical_services =  models.CharField(max_length=20, default='')
       
        active = models.BooleanField(default=True)

#--------------------------------------------------------------------------------------------------


