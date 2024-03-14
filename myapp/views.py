from django.shortcuts import render ,redirect
from . models import register, bookingfood,ADDfood,restaurant,NGOregister,feed,comp,Addemployee,Adminreg
import smtplib
import random


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')
                
# Create your views here.

def register1(request):
  if request.method =='POST':
      Firstname = request.POST.get('Firstname')
      Lastname= request.POST.get('Lastname')
      Email= request.POST.get('Emailid')
      Address= request.POST.get('Address')
      Password= request.POST.get('Password')
      Contact = request.POST.get('ContactNumber')
      register(Firstname=Firstname, Lastname=Lastname,Email=Email,Password=Password,Address=Address,Contact=Contact).save()
      return render(request,'.html') 
  else: 
    return render(request,'register.html')

       
def login(request):
   if request.method=='POST':
      Email1 = request.POST.get('Emailid')
      Password1= request.POST.get('Password')
      cr = register.objects.filter(Email=Email1,Password=Password1)
    #   print()
      if cr:
          
         details = register.objects.get(Email=Email1,Password=Password1)
         Email11  = details.Email
         
         request.session['cs'] = Email11
         return render(request,'login.html')
      else:
          return render(request,'register.html')
   else:
     return render(request,'login.html')
   


def restaurant_reg(request):
   if request.method =='POST':
      name = request.POST.get('name')
      Location= request.POST.get('Location')
      Email= request.POST.get('Emailid')
      Address= request.POST.get('Address')
      Password= request.POST.get('Password')
      Website= request.POST.get('Website')
      Contact = request.POST.get('ContactNumber')
      if restaurant.objects.filter(Email=Email):
            msge='An  Acc Already  Registerd'
            return render(request, 'restaurant_reg.html',{'mee':msge})

      else:
       restaurant(Name=name, Location=Location,Website=Website,Email=Email,Password=Password,Address=Address,Contact=Contact).save()
       return render(request,'restaurant_login.html') 
   else: 
    return render(request,'restaurant_reg.html')
  
def newfile(request):
     return render (request,'new.html')
  

def restaurant_login(request):
   if request.method=='POST':
      Email1 = request.POST.get('Emailid')
      Password1= request.POST.get('Password')
      cr = restaurant.objects.filter(Email=Email1,Password=Password1)
    #   print()
      if cr:
          
         details = restaurant.objects.get(Email=Email1,Password=Password1)
         Emaill  = details.Email
         Name=details.Name
         # print(Email11)
         request.session['mysession'] = Emaill
         request.session['resname'] = Name

         return render(request,'restaurant.html',{'Name':Name})
      else:
         if not restaurant.objects.filter(Email=Email1).exists():
            msge = 'your email is incorrect'
            return render(request, 'restaurant_login.html', {'me': msge})
         else:
            msge = 'your password is incorrect'
            return render(request, 'restaurant_login.html', {'me': msge})

   else:
     return render(request,'restaurant_login.html')


     
def restaurant_profile(request):
   ccc=request.session['mysession']
   print(ccc)
   cr=restaurant.objects.get(Email=ccc)
   pRestaurantname=cr.Name
   print(pRestaurantname)
   Location=cr.Location
   pEmailID=cr.Email
   Website=cr.Website
   pAddress=cr.Address
   pContact=cr.Contact
   return render(request,'restaurantprofile.html',{'pRestaurantname':pRestaurantname,'Email':pEmailID,'Address':pAddress,'Contact':pContact,'Location':Location,'Website': Website})


def ngoemployeprofile(request):
   ccc= request.session['username'] 
   cr=Addemployee.objects.get(username=ccc)

   Firstname=cr.name
   Lastname =cr.username 
   pEmailID=cr.Email
   pContact=cr.Contact
   return render(request,'ngoemployeprofile.html',{'Firstname':Firstname,'Lastname': Lastname ,'emailid':pEmailID,'Contact':pContact})

def ngo_profile(request):
   ccc=request.session['cs']
   cr=NGOregister.objects.get(Email=ccc)

   Firstname=cr.Firstname
   Lastname =cr.Lastname 
   pEmailID=cr.Email
   pAddress=cr.Address
   pContact=cr.Contact
   return render(request,'ngoprofile.html',{'Firstname':Firstname,'Lastname': Lastname ,'emailid':pEmailID,'Address':pAddress,'Contact':pContact})

# def restaurant_profile(request):
#      return render (request,'restaurantprofile.html')

def history (request):
     return render (request,'history.html')

# def viewdonations(request):
#      return render (request,'viewdonations.html')

def donate(request):
     return render (request,'donate.html')

def demo(request):
   if request.method=='POST':
      name=request.POST.get('name')
      item=request.POST.get('item')
      price=request.POST.get('price')
      time=request.POST.get('time')
      date=request.POST.get('date')
      demo(name=name,price=price,time=time,date=date,)
   return render(request,'demo.html')

def restaurantss(request):
   name=request.session['resname'] 
   return render(request,'restaurant.html',{'Name':name})

def addfood(request):
   if request.method=='POST':
      item=request.POST.get('name')
      qn=request.POST.get('qname')
      resname=request.POST.get('resname')
      timee=request.POST.get('time')
      datee=request.POST.get('date')
      typee=request.POST.get('type')
      dis=request.POST.get('dname')
      img=request.FILES['image']
      # status='pending'
      ADDfood(uploaded_image=img,Name=resname,cookingtime=timee,Itemname=item,Itemtype=typee,Quantity=qn,Itemdescription=dis,datee=datee).save()
      return render(request,'restaurant.html')
   else:
    resname=request.session['resname']
    return render(request,'addfood.html',{'Name':resname})
   
def donatefood(request):
   if request.method=='POST':
      item=request.POST.get('name')
      qn=request.POST.get('qname')
      timee=request.POST.get('time')
      datee=request.POST.get('date')
      typee=request.POST.get('type')
      dis=request.POST.get('dname')
      imgg=request.FILES['image']
      name='anonymous user'
      # status='pending'
      ADDfood(uploaded_image=imgg,Name=name,cookingtime=timee,Itemname=item,Itemtype=typee,Quantity=qn,Itemdescription=dis,datee=datee).save()
      return render(request,'index.html')
   else:
      return render(request,'donate.html')



# def update(request):
#    c=request.session['cs']
#    cr=register.objects.get(Email=c)
#    id=cr.id
#    pFirstname=cr.Firstname
#    pLastname=cr.Lastname
#    pEmailID=cr.Email
#    pAddress=cr.Address
#    pContact=cr.Contact
#    ppassword=cr.Password
#    return render(request,'update.html',{'Id':id,'Firstname':pFirstname,'Lastname':pLastname,'Email':pEmailID,'Address':pAddress,'Contact':pContact,'password':ppassword})

# def updateprofile(request):
#    Firstname = request.POST.get('Firstname')
#    Lastname= request.POST.get('Lastname')
#    Email= request.POST.get('Emailid')
#    Address= request.POST.get('Address')
#    Password= request.POST.get('Password')
#    Contact = request.POST.get('ContactNumber')
#    id=request.POST.get('id')
#    dt=register.objects.get(id=id)

#    dt.Firstname=Firstname
#    dt.Lastname=Lastname
#    dt.Email=Email
#    dt.Password=Password
#    dt.Address=Address
#    dt.Contact=Contact
#    dt.save()
#    return render(request,'index.html')

def NGO(request):
   name=request.session['name'] 
   return render(request,'NGO.html',{'name':name})

def NGOREGISTER(request):
  if request.method =='POST':
      Firstname = request.POST.get('Fname')
      print(Firstname)
      Lastname= request.POST.get('Lastname')
      Email= request.POST.get('Emailid')
      Address= request.POST.get('Address')
      Password= request.POST.get('Password')
      Contact = request.POST.get('ContactNumber')

      if NGOregister.objects.filter(Email=Email):
            msge='An  Acc Already  Registerd'
            return render(request, 'NGOregister.html',{'mee':msge})

      else:
         NGOregister(Firstname=Firstname, Lastname=Lastname,Email=Email,Password=Password,Address=Address,Contact=Contact).save()
         return render(request,'NGO.html') 
  else: 
    return render(request,'NGOregister.html')

def NGOlogin(request):
   if request.method=='POST':
      Email1 = request.POST.get('Emailid')
      Password1= request.POST.get('Password')
      cr = NGOregister.objects.filter(Email=Email1,Password=Password1)
    #   print()
      if cr:
          
         details = NGOregister.objects.get(Email=Email1,Password=Password1)
         Email11  = details.Email
         name=details.Firstname 
         
         request.session['cs'] = Email11
         request.session['name'] = name
         return render(request,'NGO.html',{'name':name})
      else:
         if not NGOregister.objects.filter(Email=Email1).exists():
            msge = 'your email is incorrect'
            return render(request, 'NGOlogin.html', {'me': msge})
         else:
            msge = 'your password is incorrect'
            return render(request, 'NGOlogin.html', {'me': msge})
        
   else:
     return render(request,'NGOlogin.html')

def NGOemployee(request):
   return render(request,'NGOemployee.html') 




def viewemployee(request):
   data=Addemployee.objects.all()
   return render(request,'viewemployee.html',{'data':data}) 

def NGOemployeeRegister(request):
  if request.method =='POST':
      Firstname = request.POST.get('Firstname')
      print(Firstname)
      Lastname= request.POST.get('Lastname')
      Email= request.POST.get('Emailid')
      Address= request.POST.get('Address')
      Password= request.POST.get('Password')
      Contact = request.POST.get('ContactNumber')
      NGOregister(Firstname=Firstname, Lastname=Lastname,Email=Email,Password=Password,Address=Address,Contact=Contact).save()
      return render(request,'NGOemployee.html') 
  else: 
    return render(request,'NGOemployeeregister.html')

def NGOemployeelogin(request):
   if request.method=='POST':
      username = request.POST.get('username')
      Password1= request.POST.get('Password')
      cr = Addemployee.objects.filter(username=username,Password=Password1)
    #   print()
      if cr:
          
         details = Addemployee.objects.get(username=username,Password=Password1)
         # Email11  = details.Email
         username=details.username
         request.session['username'] = username
         return render(request,'NGOemployee.html')
     
      else:
         if not  Addemployee.objects.filter(username=username).exists():
            msge = 'your username is incorrect'
            return render(request, 'NGOemployeelogin.html', {'me': msge})
         else:
            msge = 'your password is incorrect'
            return render(request, 'NGOemployeelogin.html', {'me': msge})
   else:
     return render(request,'NGOemployeelogin.html')

def addrequest(request):
   return render(request,'addrequest.html')   


def feedback(request):
   if request.method=='POST':
      name=request.POST.get('name')
      feedd=request.POST.get('dname')
      feed(name=name,feed=feedd).save()
      return render(request,'index.html')
   else:
      return render(request,'feedback.html')


def sendcomplaints(request):
   if request.method=='POST':
      name=request.POST.get('name')
      compp=request.POST.get('dname')
      comp(name=name,comp=compp).save()
      return render(request,'index.html')
   else:
      return render(request,'sendcomplaints.html')

def view_donation(request):
    res_name=request.session['resname']  
    cr=ADDfood.objects.filter(Name=res_name)
    return render(request,'view_donation.html',{'data':cr})

def delete(request,id):
   data=ADDfood.objects.get(id=id)
   data.delete()
   return redirect('view_donation')
   # return render(request,'view_donation.html')


def Addemployeess(request):
  if request.method =='POST':
      name = request.POST.get('employeename')
      username= request.POST.get('username')
      Email= request.POST.get('emailid')
      number=random.randint(10000,1000000)
      Password= 'employee' +str(number)
      Contact = request.POST.get('contact')


      s = smtplib.SMTP('smtp.gmail.com', 587)
      s.starttls()
      s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
      

      Addemployee(name=name, username=username,Email=Email,Password=Password,Contact=Contact).save()


      message = f"Congrates!!!your registration has been completed successfully.You can login using this username {username} and password {Password}"
      s.sendmail("nefsal003@gmail.com", Email, message)
      s.quit()
      return render(request,'NGO.html') 
  else: 
    return render(request,'addemployee.html')
  

  
#getting single data through id
  
def ngoviewdonation(request):
   cr=ADDfood.objects.all()
   return render(request,'ngoviewdonation.html',{'data':cr})


def foodbooking(request,item_id):
    name=request.session['name'] 
    item = ADDfood.objects.get(id=item_id)
    return render(request, 'foodbooking.html', {'item': item, 'name': name})


def save_booking(request):
   if request.method == 'POST':
        item_id = request.POST.get('item_id')
        newquantity = request.POST.get('quantity')
        remarks = request.POST.get('remarks')
        workername = request.POST.get('workername')



        item = ADDfood.objects.get(id=item_id)


        name=request.session['name'] 
       
        Name=item.Name
        Itemname=item.Itemname
        Quantity=item.Quantity
        Itemtype=item.Itemtype
        uploaded_image=item.uploaded_image
        status='waiting'

        bookingfood(Name=Name,w_status=status,workername=workername,ngoName=name,Itemname= Itemname,Quantity=Quantity, Itemtype= Itemtype, uploaded_image= uploaded_image, newquantity =newquantity,remarks= remarks).save()
        return render(request,'NGO.html')
        
   else:
      return render(request,'foodbooking.html')
   

def ngoviewrequest(request):
   name=request.session['name']
   data=bookingfood.objects.filter(ngoName=name)
   return render(request,'ngoviewrequest.html',{'data':data})


def view_donationcopy(request):
    res_name=request.session['resname']  
    print('restaurant name is',res_name)
    cr=bookingfood.objects.filter(Name=res_name)
    return render(request,'view_donation copy.html',{'data':cr})


def update_status(request,id):
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        print('id at bookingfood is',id)


        foodbooking = bookingfood.objects.get(id=id)
        resname=foodbooking.Name
      #   print(resname,'hiii')cookdoor

        RESNAME=restaurant.objects.get(Name=resname)
        print(RESNAME)
        number=RESNAME.Contact 

        ngoName=foodbooking.ngoName
        print(ngoName)
        data=NGOregister.objects.get(Firstname=ngoName)
        email=data.Email



        foodbooking.w_status = new_status
        foodbooking.save()

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()
 
 
# Authentication
        s.login("nefsal003@gmail.com","htxalvzrrkxupspv")
 
# message to be sent
        message = f" Your status has been changed to {new_status} from {resname}. For more details contact this number {number} "
 
# sending the mail
        s.sendmail("nefsal003@gmail.com",email, message)
 
# terminating the session
        s.quit()
        return render(request,'restaurant.html')
    

def viewassignedworks(request):
   username=request.session['username'] 
   data=bookingfood.objects.filter(workername=username)
   return render(request,'viewassignedworks.html',{'data':data})


def update_status_worker(request,id):
    if request.method == 'POST':
        new_status_worker = request.POST.get('new_status_worker')
        print('id at bookingfood is',id)


        foodbooking = bookingfood.objects.get(id=id)
        workername=foodbooking.workername
      #   print(resname,'hiii')cookdoor

        WORKERNAME=Addemployee.objects.get(username=workername)
        print(WORKERNAME)
        workername=WORKERNAME.name  

        ngoName=foodbooking.ngoName
        print(ngoName)
        data=NGOregister.objects.get(Firstname=ngoName)
        email=data.Email



        foodbooking.status = new_status_worker
        foodbooking.save()

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()
 
# Authentication
        s.login("nefsal003@gmail.com","htxalvzrrkxupspv")
 
# message to be sent
        message = f" Your worker {workername} has been changed their work status to {new_status_worker}"
 
# sending the mail
        s.sendmail("nefsal003@gmail.com",email, message)
 
# terminating the session
        s.quit()
        return render(request,'NGOemployee.html')

def viewemployeedelete(request,id):
   data=Addemployee.objects.get(id=id)
   data.delete()
   return redirect('viewemployee')









# ADMIN

def Addfooddelete(request,id):
   data=ADDfood.objects.get(id=id)
   data.delete()
   return redirect('adminaddfood')

def complaintsdelete(request,id):
   data=comp.objects.get(id=id)
   data.delete()
   return redirect('complaintsdelete')

def feedbackdelete(request,id):
   data=feed.objects.get(id=id)
   data.delete()
   return redirect('feedbackdelete')

def ngoregisterdelete(request,id):
   data=NGOregister.objects.get(id=id)
   data.delete()
   return redirect('ngoregisterdelete')

def addemployeedelete(request,id):
   data=Addemployee.objects.get(id=id)
   data.delete()
   return redirect('addemployeedelete')

def restaurantdelete(request,id):
   data=restaurant.objects.get(id=id)
   data.delete()
   return redirect('restaurantdelete')

def bookingfooddelete(request,id):
   data=bookingfood.objects.get(id=id)
   data.delete()
   return redirect('bookingfooddelete')

def Adminregdelete(request,id):
   data=Adminreg.objects.get(id=id)
   data.delete()
   return redirect('adminregister')




def Admin1(request):
    return render(request,'admin1.html')

def adminaddfood(request):
   data=ADDfood.objects.all()
   return render(request,'adminaddfood.html',{'data':data})

def admincomplaints(request):
   data=comp.objects.all()
   return render(request,'admincomplaints.html',{'data':data})

def adminfeedback(request):
    data=feed.objects.all()
    return render(request,'adminfeedback.html',{'data':data})

def adminngoemployeeregister(request):
    return render(request,'adminngoemployeeregister.html')
   
def adminngoregister(request):
    data=NGOregister.objects.all()
    return render(request,'adminngoregister.html',{'data':data})

def adminaddemployee(request):
    data=Addemployee.objects.all()
    return render(request,'adminaddemployee.html',{'data':data})

def adminrestaurant(request):
    data=restaurant.objects.all()
    return render(request,'adminrestaurant.html',{'data':data})

def bookingfoods(request):
    data=bookingfood.objects.all()
    return render(request,'adminbookingfoods.html',{'data':data})

def adminregister(request):
    data=Adminreg.objects.all()
    return render(request,'adminregister.html')


def adminlogin(request):
   if request.method=='POST':
      username= request.POST.get('username')
      Password1= request.POST.get('Password')
      cr = Adminreg.objects.filter(username=username,Password=Password1)
    #   print()
      if cr:
          
         details = Adminreg.objects.get(username=username,Password=Password1)
         # Email11  = details.Email
         # name=details.Firstname 
         
         # request.session['cs'] = Email11
         # request.session['name'] = name
         return render(request,'admin1.html')
      else:
         if not Adminreg.objects.filter(username=username).exists():
            msge = 'your username is incorrect'
            return render(request, 'adminlogin.html', {'me': msge})
         else:
            msge = 'your password is incorrect'
            return render(request, 'adminlogin.html', {'me': msge})
        
   else:
     return render(request,'adminlogin.html')
