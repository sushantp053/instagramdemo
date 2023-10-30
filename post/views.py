from django.shortcuts import render
from post.models import *

# Create your views here.

def post(request):
    if (request.method == "POST"):
        title = request.POST["title"]
        desc = request.POST["desc"]
        tags = request.POST["tags"]
        image = request.FILES["img"]

        Post.objects.create(title = title, postBy = request.user, tag = tags, type = 1, share_count = 0, msg = desc, media = image)


    return render(request, "post.html")