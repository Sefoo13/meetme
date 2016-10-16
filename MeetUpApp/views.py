import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from MeetUpApp.models import UserDetails


def restore_password(request):
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

def authorization(request):
    args={}
    args.update(csrf(request)) #Delete if don't need
    username = request.POST["login_field"]
    password = request.POST["pwd_field"]
    action = request.POST["action"]
    if action == "login":
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            url = reverse(account)
            return redirect(url)
        else:
            return HttpResponse('<h1>Login or password is incorrect!</h1>')
    elif action == "registration":
        email = request.POST["email_field"]
        full_name = request.POST["fullname_field"]
        try:
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            user_details = UserDetails(full_name=full_name, user=user)
            UserDetails.save(user_details)
            login(request, user)
            return redirect(reverse(account))
        except:
            return HttpResponse('<h1>Can not register!</h1>')


@login_required
def account(request):
    userId = request.user.id
    user_details = UserDetails.objects.get(user_id=userId)
    context = {'user_details':user_details}
    return render(request, "account.html", context)

@login_required
def edit_info(request, **kwargs):
    userId = kwargs['user_id']
    user_details = UserDetails.objects.get(user_id=userId)
    context = {'user_details': user_details}
    return render(request, "account_edit.html", context)

@csrf_exempt
def save_info(request):
    full_name = request.POST["fullName"]
    # birthday = request.POST["birthday"]
    city = request.POST["city"]
    country = request.POST["country"]
    description = request.POST["description"]
    userId = request.POST["userId"]
    user = UserDetails.objects.get(user_id=userId)
    user.full_name = full_name
    # user.birthday = birthday
    user.city = city
    user.country = country
    user.description = description
    user.save()
    return HttpResponse(json.dumps({'Status': 'OK'}), content_type="application/json")