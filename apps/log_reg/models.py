# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models

class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        # validate first and last name
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            if len(postData['first_name']) < 2: 
                errors['first_len'] = "Your first name needs to be two or more characters"
            if not postData['first_name'].isalpha():
                errors['first_alpha'] = "Your first name needs to be in only letters"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            if len(postData['last_name']) < 2:
                errors['last_len'] = "Your last name needs to be two or more characters"
            if not postData['last_name'].isalpha():
                errors['last_alpha'] = "Your last name needs to be in only letters"
        # validate email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

        # validate password
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors

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