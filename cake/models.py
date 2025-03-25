from django.db import models

# Create your models here.
class cake_reg(models.Model):
    fname = models.CharField(max_length=30,null =True,blank = True)
    email = models.EmailField(null=True,blank=True)
    phone = models.IntegerField()
    password = models.CharField(max_length=10,null=True,blank=True)
    cpassword = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.fname

class cake_tbl(models.Model):
    cname=models.CharField(max_length=30,null =True,blank = True)
    cimg=models.FileField(upload_to='pic',null =True,blank = True)
    cprice=models.IntegerField()

    def __str__(self):
       return self.cname


class Cart(models.Model):
    user = models.ForeignKey(cake_reg,on_delete=models.CASCADE)
    cake = models.ForeignKey(cake_tbl,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)