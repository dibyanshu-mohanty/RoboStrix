from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        message=request.POST['message']

        contact = Contact(name=name, email=email, phone=phone,address=address, message =message)
        contact.save()

        #Send Email
        send_mail(
            'Booking Inquiry',
            'There has been a Booking Inquiry for RoboStrixx. SignIn to Admin Panel for more Info.',
            'dibyanshu.m2002@gmail.com',
            ['dibyanshu2002@gmail.com','preetish.biswal2020@vitstudent.ac.in'],
            fail_silently= False,

        )
        messages.success(request,"Your Booking has been Confirmed, We will contact you soon.")
        return redirect('index')