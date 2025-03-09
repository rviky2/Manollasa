from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from core.models import *
from django.contrib import messages
from datetime import datetime





# Create your views here.
def index(request):
    category_objs = category.objects.all()
    course_objs = course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            'this is automatically generated mail from Manollasa College webpage',
            f' a person named {name} is trying to contact you\nRegarding subject:{subject}\n\n{message} \n\n return mail to: {email}',
            'manollasadisedu@gmail.com',
            ['manollasadisedu@gmail.com','manollasacollage@gmail.com'],
            fail_silently=False,
        )

        Contact = contact(name=name, email=email,
                          message=message, date=datetime.today(), subject=subject)
        Contact.save()
        messages.success(request, 'Thank you for contacting us')
        return render(request, 'index.html', {'category_objs': category_objs, 'course_objs': course_objs})
    return render(request, 'index.html', {'category_objs': category_objs, 'course_objs': course_objs})

def sikkim(request):
    return render(request, 'sikkim.html')
def magalaytan(request):
    return render(request, 'magalayatan.html')

def course_page(request):
    #try:
        if request.method == 'GET':
            ids = request.GET.get('id')
            course_obj = course.objects.get(id=ids)
            eligibility = course_obj.Eligibility.split('<>')
            return render(request, 'course.html', {'course': course_obj, 'eligibility': eligibility})
    #except:
     #   return HttpResponse("Invalid Response")


def register(request):
    course_objs = course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        branch = request.POST.get('branch')
        Register = apply(Name=name, Email=email, Place=place,
                           Phone=phone, Branch=branch, date=datetime.today())
        Register.save()
        send_mail(
            'this is computer generated mail from Manollasa College webpage',
            f' Name: {name}\nEmail: {email}\n place: {place}\nPhone: {phone}\n Branch: {branch} \n',
            'manollasacollage@gmail.com',
            ['adarshsavaligi@gmail.com','manollasacollage@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Form submission successful')
        return render(request, 'Apply.html',{'course_objs':course_objs})
    return render(request, 'Apply.html',{'course_objs':course_objs})





import hmac
import hashlib
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# CI/CD pipeline 
@csrf_exempt  
def github_webhook(request):
    if request.method == 'POST':
        secret = 'manollasa' 

        signature = request.headers.get('X-Hub-Signature')

        if not signature:
            return HttpResponseBadRequest("Signature missing")

        body = request.body
        hashed_signature = hmac.new(secret.encode(), body, hashlib.sha1).hexdigest()
        computed_signature = f"sha1={hashed_signature}"

        if hmac.compare_digest(computed_signature, signature):

            import subprocess
            subprocess.run(['git', 'pull', 'origin', 'main'])
            subprocess.run(['docker-compose', 'build'])
            subprocess.run(['docker-compose', 'restart'])

            return HttpResponse("Payload received and verified!", status=200)
        else:
            return HttpResponseBadRequest("Invalid signature")
    else:
        return HttpResponseBadRequest("Invalid request method")

