from django.db import models

# Create your models here.
class App(models.Model):
    appname=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    developer=models.CharField(max_length=250)
    size=models.CharField(max_length=50)
    def __str__(self):
        return self.appname

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    desg=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Review(models.Model):
     appname=models.ForeignKey(App,related_name='app',on_delete=models.CASCADE)
     username=models.ForeignKey(User,related_name='uname',on_delete=models.CASCADE)
     review=models.CharField(max_length=250)
     rating=models.CharField(max_length=250)
     

class blockwords(models.Model):
    blockwords=models.CharField(max_length=50)
    def __str__(self):
        return self.blockwords



class Work(models.Model):   
    workname=models.CharField(max_length=25)
    workprogres=models.CharField(max_length=25)    
    def __str__(self):
        return self.workname 


class WorkAssign(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    workname=models.ForeignKey(Work,on_delete=models.CASCADE)
    workDate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.workname)

class WorkProgress(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    work=models.ForeignKey(WorkAssign,on_delete=models.CASCADE)
    detail=models.CharField(max_length=50)
    workDate = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50)
    def __str__(self):
        return str(self.workDate)