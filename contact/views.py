from django.shortcuts import render,redirect
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing_name']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

        #checking user already made contact
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contacts.objects.filter(listing_id=listing_id,user_id=user_id) 
            if has_contacted:
                messages.error(request,"You have already made inquiry about this property")
                return redirect("/listings/"+listing_id)
        contact = Contacts(listings=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()
        messages.success( request,"Your inquiry is submitted")
#         send_mail(
#     'New Proprty Inquiry from {}'.format(name),
#     'There is a new inquiry about {} ,please visit admin panel for more info '.format(listing),
#     'kkthunga1@gmail.com',
#     ['kota.karthikthunga803@gmail.com',realtor_email],
#     fail_silently=False,
# )
    
        return redirect("/listings/"+listing_id)

