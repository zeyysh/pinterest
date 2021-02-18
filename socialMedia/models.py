import datetime
from time import timezone

from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=128, null=True)
    age = models.IntegerField(default=0, blank=True)
    password = models.CharField(max_length=128, null=True)
    email = models.EmailField(verbose_name='email field', max_length=60, unique=True)
    photo = models.ImageField(blank=True)
    location = models.TextField(blank=True, default=" ")
    website = models.URLField(blank=True)
    gender = models.TextChoices()
    follower = models.ManyToOneRel(User)
    following = models.ManyToOneRel(User)
    report = models.TextField(blank=True)
    #date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    #last_login = models.DateTimeField(verbose_name='date joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def sign_up(self, email, username, password):
        return User

    def login(self, email, password):
        return User

    def check_user_info(self, **args):
        return True

    def recieve_user_info_for_block(self, id):
        return User.id

    def block_user(self, user):
        return User
