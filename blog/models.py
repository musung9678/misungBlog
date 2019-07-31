from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self):
        return self.title #타이틀만드는방법

        # Create your models here.
    def summary(self):
        return self.body[:50]

        #글자수를 리턴합시다