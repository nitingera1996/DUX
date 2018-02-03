from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from bookmyguide.models import *

def IndexView(request):
	places_list = Places.objects.order_by('-likes')[:10]
	for place in places_list:
		place.url = place.name.replace(' ', '_')
	template_name = 'index.html'
	return render(request,template_name,{'places':places_list})

def LoginView(request):
	pass

def RegisterView(request):
	if request.method == "POST":
		full_name = request.POST.get('full_name', '')
		mobile_no = request.POST.get('mobile_no', '')
		email = 'abc@def.com'
		password = request.POST.get('password', '')

		try:
			user = User.objects.create_user(mobile_no, email, password)
			user.save()
		except:
			template_name = 'register.html'
			return render(request,template_name,{'error':'User already exist'})

		dP = DuxProfile(user=user,full_name=full_name,mobile_number=mobile_no,profile_photo="/static/photo.png")
		dP.save()

		user = authenticate(username='john', password='secret')
		if user:
			if user.is_active:
				login(request, user)
		template_name = 'index.html'
		return render(request,template_name,{})
		
	else:
		template_name = 'register.html'
		return render(request,template_name,{})
