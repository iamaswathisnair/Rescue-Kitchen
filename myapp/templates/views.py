from django.shortcuts import render ,redirect
from . models import register,ADDfood,restaurant,NGOregister,feed,comp

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
                msge='your email is incorrect'
                return render(request,'restaurant_login.html',{'me':msge})
            else:
                msge='your password is incorrect'
                return render(request,'restaurant_login.html',{'me':msge})
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
   return render(request,'restaurant.html')

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
      status='pending'
      ADDfood(uploaded_image=img,Name=resname,cookingtime=timee,status=status,Itemname=item,Itemtype=typee,Quantity=qn,Itemdescription=dis,datee=datee).save()
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
      status='pending'
      ADDfood(uploaded_image=imgg,Name=name,cookingtime=timee,status=status,Itemname=item,Itemtype=typee,Quantity=qn,Itemdescription=dis,datee=datee).save()
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
   return render(request,'NGO.html') 

def NGOREGISTER(request):
  if request.method =='POST':
      Firstname = request.POST.get('Fname')
      print(Firstname)
      Lastname= request.POST.get('Lastname')
      Email= request.POST.get('Emailid')
      Address= request.POST.get('Address')
      Password= request.POST.get('Password')
      Contact = request.POST.get('ContactNumber')
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
         
         request.session['cs'] = Email11
         return render(request,'NGO.html')
      else:
          return render(request,'NGOregister.html')
   else:
     return render(request,'NGOlogin.html')

def NGOemployee(request):
   return render(request,'NGOemployee.html') 

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
      Email1 = request.POST.get('Emailid')
      Password1= request.POST.get('Password')
      cr = NGOregister.objects.filter(Email=Email1,Password=Password1)
    #   print()
      if cr:
          
         details = NGOregister.objects.get(Email=Email1,Password=Password1)
         Email11  = details.Email
         
         request.session['cs'] = Email11
         return render(request,'NGOemployee.html')
      else:
          return render(request,'NGOemployeeregister.html')
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

def sendfeedback(request):
   if request.method=='POST':
      name=request.POST.get('name')
      feed=request.POST.get('dname')
      feed(name=name,feed=feed).save()
      return render(request,'index.html')
   else:
      return render(request,'sendcomplaints.html')

def view_donation(request):
    res_name=request.session['resname']  
    cr=ADDfood.objects.filter(Name=res_name)
    return render(request,'view_donation.html',{'data':cr})

def delete(request,id):
   data=feed.objects.get(id=id)
   data.delete()
   return redirect('view_donation')
   # return render(request,'view_donation.html')

def Addfooddelete(request,id):
   data=ADDfood.objects.get(id=id)
   data.delete()
   return redirect('adminaddfood')

def complaintsdelete(request,id):
   data=comp.objects.get(id=id)
   data.delete()
   return redirect('complaintsdelete')

def feedbackdelete(request,id):
   data=comp.objects.get(id=id)
   data.delete()
   return redirect('feedbackdelete')


def view_donationcopy(request):
    res_name=request.session['resname']  
    cr=ADDfood.objects.filter(Name=res_name)
    return render(request,'view_donation copy.html',{'data':cr})

def ngoviewdonation(request):
   cr=ADDfood.objects.all()
   return render(request,'ngoviewdonation.html',{'data':cr})

def Admin1(request):
    return render(request,'admin1.html')

def adminaddfood(request):
   data=ADDfood.objects.all()
   return render(request,'adminaddfood.html',{'data':data})

def admincomplaints(request):
   data=comp.objects.all()
   return render(request,'admincomplaints.html',{'data':data})

def adminfeedback(request):
    return render(request,'adminfeedback.html')

def adminngoemployeeregister(request):
    return render(request,'adminngoemployeeregister.html')
   
def adminngoregister(request):
    return render(request,'adminngoregister.html')

def adminrestaurant(request):
    return render(request,'adminrestaurant.html')