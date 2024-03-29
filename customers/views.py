from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from . models import Customer

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST :
        context['register'] = True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            address=request.POST.get('address')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            # create user account
            user=User.objects.create_user(
                username=username, 
                password=password,
                email=email
            )
            # create customer account
            customer=Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address,
            )
            success_message="user registered successfully"
            messages.success(request,success_message)
            context
        except Exception as e:
            error_message="Duplicate username or invalid inputs"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST :
        context['register'] = False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user credentials')
    return render(request, 'account.html',context)
#def pdf_pront(request):
    # Create a file-like buffer to receive PDF data.
  #  buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
   # p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
   # username
    # Close the PDF object cleanly, and we're done.
  #  p.showPage()
    #p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    #buffer.seek(0)
    #return FileResponse(buffer, as_attachment=True, filename='hello.pdf')