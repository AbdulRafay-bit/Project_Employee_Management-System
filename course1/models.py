from django.db import models
from django.contrib.auth.models import User

class EmployeeDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    empcode=models.CharField(max_length=58)
    empdept=models.CharField(max_length=158,null=True)

    designation=models.CharField(max_length=108,null=True)
    contact=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=58,null=True)
    joiningate=models.DateField(null=True)

    def __str__(self):
        return self.user.username
    

# Create your models here.
