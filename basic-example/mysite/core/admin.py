from django.contrib import admin
from .models import PollBlockchain, Poll, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class PollBlockchainAdmin():
    admin.site.register(PollBlockchain)


class PollAdmin():
    admin.site.register(Poll)


class UserProfileAdmin():
    admin.site.register(UserProfile)

    

   

