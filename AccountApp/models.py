from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.core.validators import MinLengthValidator,M, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
class User(AbstractUser):
    pass
number_validator=RegexValidator(
    regex=r'^\d{8}$',
    message="le numéro doit contenir 8 chiffres"
)
def birth_date_validator(d):
    if d>= timezone.localdate():
        raise ValidationError("La date de naissance doit être antérieure à la date actuelle.")
class Doctor (User):
    license_number = models.CharField(max_length=6,unique=True, validators=[number_validator])
    phone= models.CharField(max_length=8,validators=[number_validator])
    specialty = models.ManyToManyField("AccountApp.Specialty", related_name="doctors")

class Patient (User):
    national_id = models.CharField(max_length=8,unique=True, validators=[number_validator])
    phone= models.CharField(max_length=8,validators=[number_validator]) 
    birth_date = models.DateField(birth_date_validator)

class Specialty(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
