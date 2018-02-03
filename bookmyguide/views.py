from django.shortcuts import render

def IndexView(request):
    template_name = 'index.html'
    return render(request,template_name,{})

def LoginView(request):
	pass

def RegisterView(request):
	pass
