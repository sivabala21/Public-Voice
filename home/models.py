from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def upvote(self):
        self.upvotes += 1
        self.save()

    def downvote(self):
        self.upvotes -= 1
        self.save()
