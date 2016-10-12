from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse


def restore_password(request):
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

def auth(request):

    username = request.POST["login_field"]
    password = request.POST["pwd_field"]
    action = request.POST["action"]
    if action == "login":
        user = authenticate(username=username, password=password)
        if user:
            url = reverse(account)
            return  redirect(url, user = user)
        else:
            return HttpResponse('<h1>Login or password is incorrect!</h1>')
    elif action == "registration":
        email = request.POST["email_field"]
        User.objects.create_user(username, email, password)

@login_required
def account(request):
    userId = request.user.id
    user = User.objects.get(id=userId)
    pass

