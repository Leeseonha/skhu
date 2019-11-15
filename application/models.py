from django.db import models
from account.models import User

class Application(models.Model):
    title = models.CharField(max_length=100) # 지원서 제목
    body1 = models.TextField() # 지원서 답변1
    body2 = models.TextField() # 지원서 답변2
    body3 = models.TextField() # 지원서 답변3
    body4 = models.TextField() # 지원서 답변4
    body5 = models.TextField() # 지원서 답변5
    body6 = models.TextField() # 지원서 답변6
    pub_date = models.DateTimeField('date published') # 올린 시간
    attachment = models.FileField(upload_to='documents/', null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return self.title

    
    