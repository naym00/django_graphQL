from django.db import models
from helps.choice import common as CHOICE
from django.contrib.auth.models import AbstractUser
from helps.common.generic import Generichelps as ghelp

def generate_unique_code():
    return ghelp().getUniqueCodePattern()

def upload_user_photo(instance, filename):
    return "files/user/{username}/photo/{unique}_{filename}".format(username=instance.username, unique=generate_unique_code(), filename=filename)

class Grade(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Designation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Shift(models.Model):
    name = models.CharField(max_length=50, unique=True)
    in_time = models.TimeField()
    out_time = models.TimeField()

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Religion(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.id} - {self.name}'

class User(AbstractUser):
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True, related_name='designation_users')
    gender = models.CharField(max_length=10, choices=CHOICE.GENDER, blank=True, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, blank=True, null=True, related_name='religion_users')
    phone = models.CharField(max_length=14, unique=True, blank=True, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_shift')
    photo = models.ImageField(upload_to=upload_user_photo, blank=True, null=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='createdby_users')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='updatedby_users')
    
    def __str__(self):
        return f'{self.id} - {self.username} - {self.is_active}'

class Ethnicgroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.ManyToManyField(User, blank=True, related_name='user_ethnicgroups')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='createdby_ethnicgroups')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updatedby_ethnicgroups')

    def __str__(self):
        return f'{self.id} - {self.name}'

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note_users')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='createdby_notes')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updatedby_notes')
    def __str__(self):
        return f'{self.id} - {self.title} - {self.user.username}'