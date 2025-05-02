from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *

def index(request):
    if request.method=='POST':
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        obj=cake_reg.objects.create(fname = name,phone = phone,email = email,password = password,cpassword=cpassword) 
        obj.save()
        if obj:
            return redirect(login_view)
        else:
            return render(request,'register.html')  
    return render(request,'register.html')

def login_view(request):
    if request.method =='POST':
        eml = request.POST.get('email')
        pas = request.POST.get('pass')
        obj=cake_reg.objects.filter(email=eml,password=pas)
        print(eml)
        print(pas)
        if obj:
          for ls in obj:
            idno=ls.id
          request.session['idl']=idno
          request.session['ema']=eml
          request.session['psa']=pas
          return render(request,'home.html')
        else:
            msg = 'invalid email and password'
        request.session['ema']=''
        request.session['psa']=''
        return render(request,'login_view.html',{'msg':msg})
    else:
      return render(request,'login_view.html')
     

def cake_upld(request):
  if request.method=='POST':
    cname = request.POST.get('cname')
    cimage = request.FILES.get('cimage')
    cprice=request.POST.get('cprice')
    obj=cake_tbl.objects.create(cname=cname,cimg=cimage,cprice=cprice)
    obj.save()
    if obj:
      msg='file uploaded'
      return redirect(cake_view_all)
    else:
       return render(request,'cake.html')       
  return render (request,'cake.html')
def cake_view_all(request):
   data=cake_tbl.objects.all()
   return render (request,'cakeview.html',{'data':data})


def addtocart(request):
   pro=request.GET.get('idn')
   usr=request.session['idl']
   pobj=cake_tbl.objects.get(id=pro)
   cobj=cake_reg.objects.get(id=usr)
   cartitem,created=Cart.objects.get_or_create(user=cobj,cake=pobj)
   if not created:
      cartitem.quantity+=1
      cartitem.save()
   return redirect(viewcart)


def viewcart(request):
   idno = request.session['idl']
   cuobj=cake_reg.objects.get(id=idno)
   cartobj=Cart.objects.filter(user=cuobj)
   if cartobj:
      total_price = 0
      total_qt = 0
      for i in cartobj:
         pro= i.cake.cprice*i.quantity
         total_price = total_price+pro
         total_qt = total_qt + i.quantity
      return render(request,'cart.html',{'cart_items':cartobj,'total_price':total_price,'total_qt':total_qt})
   else:
      return render(request,'cart.html',{'info':'CART IS EMPTY'})
   
def cartdel(request):
   num = request.GET.get('cid')
   obj=Cart.objects.filter(id=num)
   obj.delete()
   return redirect(viewcart)

def home(request):
   return render (request,'home.html')


from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
  

def send_cake_email(request, cake_id):
    if request.method == "POST":
        recipient_email = request.POST.get("recipient_email")
        cake = get_object_or_404(cake_tbl, id=cake_id)

        subject = f"Check out this Cake: {cake.cname}"
        
        # Embed the image URL in the email
        message = f"""
        <html>
            <body>
                <h2>Hey! Check out this amazing cake:</h2>
                <p><strong>🍰 Name:</strong> {cake.cname}</p>
                <p><strong>💰 Price:</strong> ${cake.cprice}</p>
                <img src="{{cake.cimg.url}}" alt="Cake Image" width="300" style="border-radius:10px;">
            </body>
        </html>
        """

        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, "", email_from, [recipient_email], html_message=message)

        return redirect("cakeview")