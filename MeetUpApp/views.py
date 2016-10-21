import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from MeetUpApp.models import UserDetails, Trip
from MeetUpApp.enums import days, months, years


def restore_password(request):
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()

def authorization(request):
    username = request.POST['login_field']
    password = request.POST['pwd_field']
    action = request.POST['action']
    if action == "login":
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            url = reverse(account)
            return redirect(url)
        else:
            return HttpResponse('<h1>Login or password is incorrect!</h1>')
    elif action == "registration":
        email = request.POST['email_field']
        full_name = request.POST['fullname_field']
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
    context = {'user_details': user_details}
    try:
        trips = Trip.objects.filter(user_id=userId)
        trips_number = trips.count()
        context['trips'] = trips
        context['trips_number'] = trips_number
    except:
        trips_number = 0
        context['trips_number'] = trips_number
    return render(request, "account.html", context)

@login_required
def edit_info(request, **kwargs):
    userId = kwargs['user_id']
    user_details = UserDetails.objects.get(user_id=userId)
    user_day = UserDetails.get_day(user_details)
    user_month = UserDetails.get_month(user_details)
    user_year = UserDetails.get_year(user_details)

    context = {
        'user_details': user_details,
        'days':days,
        'months':months,
        'years':years,
        'user_day':"0"+str(user_day),
        'user_month':"0"+str(user_month),
        'user_year':user_year
    }
    return render(request, "account_edit.html", context)

@csrf_exempt
def save_info(request):
    action = request.POST['action']
    if action == "user_details":
        full_name = request.POST['fullName']
        birthday = request.POST['birthday']
        city = request.POST['city']
        country = request.POST['country']
        description = request.POST['description']
        user_id = request.POST['userId']
        user = UserDetails.objects.get(user_id=user_id)
        user.full_name = full_name
        user.birthday = birthday
        user.city = city
        user.country = country
        user.description = description
        user.save()
        return HttpResponse(json.dumps({'Status': 'OK'}), content_type="application/json")

    elif action == "agree_to_meet":
        user_id = request.POST['userId']
        agree_to_meet = request.POST['agreeToMeet']
        if agree_to_meet == "true":
            agree_to_meet = True
        else:
            agree_to_meet = False
        user = UserDetails.objects.get(user_id=user_id)
        user.agree_to_meet = agree_to_meet
        user.save()
        return HttpResponse(json.dumps({'Status': 'OK'}), content_type="application/json")

def save_trip(request):
    date_arrive = request.POST['arrive_field']
    date_leave = request.POST['leave_field']
    country = request.POST['country_field']
    city = request.POST['city_field']
    description = request.POST['description_field']
    userId = request.user.id
    user = User.objects.get(id=userId)
    trip = Trip(description=description, country=country, city=city, date_arrive=date_arrive, date_leave=date_leave, find_local=False, user=user)
    trip.save()
    return redirect('/account')