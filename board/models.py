from django.db import models
from account.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    notice_or_not = models.BooleanField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    board_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body[:10]