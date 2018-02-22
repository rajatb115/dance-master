from django.shortcuts import render,render_to_response,get_object_or_404
from .models import Registration,notice

# Create your views here.
def home(request):
    return render_to_response('home/index.html',{
        'notices':notice.objects.all(),
    })

def contact_us(request):
    return render(request,'home/contactus.html')

def registration(request):
	return render(request,'paypal/payment.html',{'registrations': Registration.objects.all(),})

def rentourspace(request):
	return render(request,'home/rentourspace.html')
