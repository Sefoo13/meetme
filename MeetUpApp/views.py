from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def restore_password(request):
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

def auth(request):

    username = request.POST['login_field']
    password = request.POST['pwd_field']
    action = request.POST['action']
    if action == "login":
        user = authenticate(username=username, password=password)
    elif action == "registration":
        email = request.POST['email_field']
        User.objects.create_user(username, email, password)





    # if user is not None:
    #     # the password verified for the user
    #     if user.is_active:
    #         print("User is valid, active and authenticated")
    #     else:
    #         print("The password is valid, but the account has been disabled!")
    # else:
    #     # the authentication system was unable to verify the username and password
    #     print("The username and password were incorrect.")