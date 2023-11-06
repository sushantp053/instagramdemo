import uuid
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    uid = models.UUIDField(primary_key=True, unique=True,
                           editable=False, default=uuid.uuid4)
    title = models.TextField()
    postBy = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    tag = models.TextField()
    type = models.IntegerField()
    share_count = models.BigIntegerField(default=0)
    msg = models.TextField()
    media = models.ImageField(upload_to="media")

    def __str__(self) -> str:
        return str(self.uid)


class Like(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField()


class Mention(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    mention_to = models.ForeignKey(User, on_delete=models.CASCADE)
