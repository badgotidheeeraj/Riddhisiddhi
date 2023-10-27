from django.db import models

# Create your models here.



class send_data(models.Model):
    FullName=models.CharField(max_length=1000)
    Email=models.EmailField(max_length=50)
    PhoneNumber =models.IntegerField()
    Name=models.TextField()
    # def __unicode__(self):



class dynamic_data(models.Model):
    about=models.TextField()
    howtowork=models.TextField()
    title=models.TextField()
    banner=models.TextField()
    Adress=models.TextField()
    admin=models.TextField()