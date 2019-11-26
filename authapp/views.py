import json
import random
import http.client
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Register
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm, SigninForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        regform = SignupForm(request.POST)
        if regform.is_valid():
            x = otp_send(request)
            if x:
                return render(request, 'otp_input.html')
            else:
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html')
    else:
        # regform =User_regform()
        return render(request, 'signup.html')


def otpvalidation(request):
    newotp = request.POST["otp"]
    oldotp = request.session["otp"]
    if newotp == oldotp:
        form = SignupForm(request.session["details"])
        new_user = User.objects.create_user(username=request.session["uname"], password=request.session["pwd"])
        new_user.save()
        form.save()
        login(request, new_user)
        return render(request, "auth_home.html")
    else:
        return render(request, 'otp_input.html')


def otp_send(request):
    print("print otp")
    ot = str(random.randint(100000, 999999))
    # request.session["pwd"]=request.POSt["t1]
    mobno = request.POST["mobno"]
    print("otp")
    # temail=request.POST["email"]
    request.session["uname"] = request.POST["uname"]
    request.session["pwd"] = request.POST["pwd"]
    # subject="registration otp"
    # From_mail=settings.EMAIL_HOST_USER
    # to_list=[temail]
    # send_mail(subject, ot, From_mail, to_list, fail_silently=False)
    # print("otp sent to mail")
    request.session["details"] = request.POST
    request.session["otp"] = ot
    conn = http.client.HTTPConnection("api.msg91.com")
    payload = "{\"sender\":\"RAJATH\", \"route\": \"4\", \"country\": \"91\", \"sms\": [{\"message\":\"" + ot + "\", \"to\": [\"" + mobno + "\"]}]}"
    headers = {
        'authkey': "300681AoXgnUT65db19e51",
        'content-type': "application/json"
    }
    conn.request("POST",
                 "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&aferminute=&response=&campaign=",
                 payload, headers)
    data = conn.getresponse()
    res = json.loads(data.read().decode("UTF-8"))
    print(res)
    if res["type"] == "success":
        return True
    else:
        return False


@login_required
def login(request):
    return render(request, "auth_home.html")


def my_logout(request):
    logout(request)
    return render(request, 'index.html')
