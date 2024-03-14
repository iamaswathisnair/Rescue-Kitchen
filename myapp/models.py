from django.db import models
r_choice=(('pending','pending'),('done','done'),('over','over'))
w_choice=(('waiting','waiting'),('Request Accepted','Request Accepted'),('Request Denied','Request Denied'))



# Create your models here.
class register(models.Model):
 Firstname = models.CharField(max_length=30)
 Lastname = models.CharField(max_length=30)  
 Email  = models.EmailField()
 Password = models.CharField(max_length=30)
 Address = models.CharField(max_length=30)
 Contact = models.IntegerField() 

class restaurant(models.Model):
  Name = models.CharField(max_length=30)
  Location  = models.CharField(max_length=30)
  Email=models.EmailField()
  Password = models.CharField(max_length=30)
  Website=models.CharField(max_length=30)
  Address=models.CharField(max_length=30)
  Contact = models.IntegerField()
# image= models.ImageField(max_length=30)

class ADDfood(models.Model):
  Name = models.CharField(max_length=300)
  Itemname= models.CharField(max_length=100)
  Quantity = models.IntegerField()
  Itemtype=models.CharField(max_length=100,null='true')
  Itemdescription= models.CharField(max_length=30,)
  cookingtime=models.TimeField(null=True)
  datee=models.DateTimeField(null=True)
  uploaded_image=models.FileField(upload_to='add_food/')
  

class NGOregister(models.Model):
  Firstname = models.CharField(max_length=30)
  Lastname = models.CharField(max_length=30)  
  Email  = models.EmailField()
  Password = models.CharField(max_length=30)
  Address = models.CharField(max_length=30)
  Contact = models.IntegerField() 

class NGOemployeeregister(models.Model):
  Firstname = models.CharField(max_length=30)
  Lastname = models.CharField(max_length=30)  
  Email  = models.EmailField()
  Password = models.CharField(max_length=30)
  Address = models.CharField(max_length=30)
  Contact = models.IntegerField() 

class feed(models.Model):
  name=models.CharField(max_length=30)
  feed=models.CharField(max_length=500)

class comp(models.Model):
  name=models.CharField(max_length=30)
  comp=models.CharField(max_length=500)

class Addemployee(models.Model):
 name = models.CharField(max_length=30)
 username = models.CharField(max_length=30)  
 Email  = models.EmailField()
 Password = models.CharField(max_length=30)
 Contact = models.IntegerField()


class bookingfood(models.Model):
  ngoName = models.CharField(max_length=300)
  Name = models.CharField(max_length=300)
  workername = models.CharField(max_length=300)
  Itemname= models.CharField(max_length=100)
  Quantity = models.IntegerField()
  Itemtype=models.CharField(max_length=100,null='true')
  uploaded_image=models.FileField()
  newquantity = models.IntegerField()
  remarks= models.CharField(max_length=500)
  w_status=models.CharField(max_length=30,choices=w_choice)
  status=models.CharField(max_length=200,choices=r_choice)



class Adminreg(models.Model):
 username = models.CharField(max_length=30)  
 Password = models.CharField(max_length=30)

