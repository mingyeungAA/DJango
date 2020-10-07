from django.db import models


# models상속받음
# MyBoard라는 테이블 만들어짐
class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateField('date published')
