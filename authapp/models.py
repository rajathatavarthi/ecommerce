from django.db import models
class Register(models.Model):
    name= models.CharField(primary_key=True,max_length=10)
    mobno = models.IntegerField()
    email= models.EmailField()
    uname= models.CharField(max_length=10)
    pwd= models.CharField(max_length=10)
    cpwd= models.CharField(max_length=10)

class Signin(models.Model):
    uname = models.CharField(primary_key=True,max_length=10)
    pwd = models.CharField(max_length=10)
    def get_user(self):
        return self.uname
    def get_pwd(self):
        return self.pwd


