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
    gender = models.TextField()
    follower = models.IntegerField()
    following = models.IntegerField()
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


class Comment(models.Model):
    report = models.TextField(max_length=1000)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=False)
    pin_key = models.ForeignKey('Pin', on_delete=models.CASCADE, null=True, blank=False)
    content = models.TextField(null=True)
    like_status = models.IntegerField(default=0, blank=False)
    picture = models.ImageField()

    def try_comment(self, picture, user, pin):
        return picture

    def write_comment(self, user, pin, txt):
        return txt


class Board(models.Model):
    notes = models.CharField(max_length=200, blank=True)
    keep_secret = models.BooleanField(blank=False)
    description = models.CharField(blank=True, max_length=300)
    board_key = models.ForeignKey('Board', on_delete=models.CASCADE, null=True, blank=False)
    board_id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=200,)
    user_key = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=False)
    collaborators = models.ForeignKey('Pin', on_delete=models.CASCADE, null=True, blank=False)

    def create_board(self, name, user):
        return name

    def add_pin_to_board(self, name, user, pin):
        return pin

    def edit_board(self, name, user):
        return name

    def delete_board(self, name, user):
        return name


class Pin(models.Model):
    photo = models.BinaryField()
    video = models.BinaryField()
    board_key = models.ForeignKey('Board', blank=False, on_delete=models.CASCADE, null=True)
    user_key = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=False)
    comment_key = models.ForeignKey('Comment', blank=False, on_delete=models.CASCADE, null=True)
    pin_id = models.IntegerField(primary_key=True, blank=False)
    pin_link = models.URLField()
    pin_date = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=200,)
    report = models.CharField(max_length=200,)
    website_link = models.URLField()
    order_in_board = models.IntegerField(blank=False)

    def create_pin(self, user, picture):
        return picture

    def delete_pin(self, user, picture):
        return picture


class Massage(models.Model):
    photo = models.ImageField(blank=True)
    massage_id = models.IntegerField(primary_key=True, blank=False)
    text = models.CharField(max_length=200,)
    sender = models.ForeignKey('User', blank=False, on_delete=models.CASCADE)
    #receiver = models.ForeignKey('User', blank=False, on_delete=models.CASCADE)
    massage_date = models.DateTimeField(auto_now_add=True)

    def send_massage(self, user1, user2, text, photo):

        return user1

    def recieve_massage(self, user1, user2, text, photo):

        return user2


class Report(models.Model):
    report_type = models.CharField(max_length=200, blank=False)
    report_id = models.IntegerField(primary_key=True, blank=False)
    report_date = models.DateTimeField(auto_now_add=True)

    def get_report(self,report):

        return report


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    category_id = models.IntegerField(primary_key=True, blank=False)
