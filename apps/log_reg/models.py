# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, first_name, last_name, email, password):
        errors = []
        if first_name == "":
            errors.append("First name cannot be empty")
        if last_name == "":
            errors.append("Last name cannot be empty")
        if email == "":
            errors.append("Email cannot be empty")
        if password == "":
            errors.append("Password cannot be empty")
        return (False, errors)
    def validateLogin(self, email, password):
        errors = []
        if email == "":
            errors.append("Email cannot be empty")
        elif len(User.objects.filter(email=email)) > 0:
            errors.append("Email already exists, try again.")
        if password == "":
            errors.append("Password cannot be empty")
        if len(errors) == 0:
            return (False, errors)
        else:
            users = self.filter(email=email)
            if len(users) > 0:
                user = users[0]
                if user.password == password:
                    return (True, user.id)
                else:
                    errors.append("Password incorrect, try again.")
            else:
                errors.append(request, "No email found")
        return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.first_name + " " + self.last_name