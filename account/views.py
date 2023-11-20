from click import UUID
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.models import *
from django.db.models import Count

from django.contrib import messages

# Create your views here.


def changeLike(request, likeid):
    # print(likeid)
    post = Post.objects.get(uid=likeid)

    Like.objects.create(postId=post, like_by=request.user)

    return redirect("/home")


def demoApi(request):
    post = request.POST["next"]

    return JsonResponse({"name": "sagar", "age": 23})


def login1(request):
    # if (request.user != None):
    #     return redirect("/home")
    if (request.method == "POST"):
        email = request.POST["email"]
        password = request.POST["pass"]

        next = request.POST["next"]

        user = authenticate(username=email, password=password)

        if (user != None):
            login(request, user)

            if (next != "" and next != None):
                return redirect(next)

            return redirect("/home")
        else:

            print("user login not successfull")
            messages.error(request, "User credintials are wrong.")
            if (next != ""):
                fs = "hello {1}"
                return redirect(f"login?next={next}")
            else:
                return render(request, "login.html")

    return render(request, "login.html")


@login_required
def home(requst):

    # allPost = Post.objects.all()
    allPost = Post.objects.all().annotate(
        Count('like'), Count('comment', distinct=True))
    likePost = Like.objects.filter(like_by=requst.user)

    print("like post data", likePost)

    return render(requst, "home.html", context={"allpost": allPost, "likepost": likePost})


def register(request):

    return render(request, "registration.html")


def registration(request):
    if (request.method == "POST"):
        email = request.POST["email"]
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        password = request.POST["pass"]

        if (User.objects.filter(username=email).exists()):
            messages.success(request, "User already exist")
            return render(request, "registration.html")

        user = User.objects.create(
            username=username, first_name=fullname,
            email=email, password=password)

        user.set_password(password)
        user.save()
        messages.success(request, "Successfully registered please login")
        return render(request, "login.html")

    return HttpResponse("<h1>Invalid Url</h1>")
