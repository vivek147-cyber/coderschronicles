from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import contactform,training_course,projects
from django.contrib import messages

# Create your views here.

def index(request):
   if request.method == 'POST' and 'contactforquery' in request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        contactNumber=request.POST.get('phonenumber')
        message=request.POST.get('message')
        

        contact = contactform(
            name=name,
            email=email,
            contactNumber=contactNumber,
            message=message,
            
        )

        contact.save()
        messages.success(request, 'Form is successfully submitted.You will be contact soon.Thankyou :)')
        return HttpResponseRedirect('/#contact') 
   return render(request,'index.html')



def course(request):

  tcourse=training_course.objects.all();
  return render(request,'course.html',{'tcourse':tcourse })



def about(request):

#  teachers=teacher.objects.all();

 return render(request,'about.html')

def project(request):

 project=projects.objects.all();
 return render(request,'project.html',{'project':project})

