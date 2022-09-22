from django.db import models

# Create your models here.

class Fan(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi



class Student(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    yosh = models.IntegerField()
    sana = models.DateField()
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)




class Fans(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi



class Teach(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    yosh = models.IntegerField()
    sana = models.DateField()
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
