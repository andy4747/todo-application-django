from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class EmailAuthBackend(BaseBackend):
    """
    Email Authentication Backend

    Using email/password pair to login rather than username/password pair
    """
    def authenticate(self,request,email=None,password=None):
        login_valid=(settings.ADMIN_LOGIN==email)
        pwd_valid=check_password(password,settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExists:
                user=User(email=email)
                user.is_staff=True
                user.is_superuser=True
                user.save()
            return user
        return None


    def get_user(self,user_id):
        """
        Gets a User objects from the user_id.
        """
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExists:
            return None