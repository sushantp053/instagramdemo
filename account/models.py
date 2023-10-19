from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    


class Friend(models.Model):
    user_id = models.TextField()
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE)

