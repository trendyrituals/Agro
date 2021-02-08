from django.shortcuts import render,redirect
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	)
from .forms import Signup_Form, Login_Form
# from django.contrib.auth.models import User

# Create your views here.
def home(request):

	return render(request,'home.html',{})

def login_v(request):
	form = Login_Form(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		try:
			login(request,user)
			return redirect('/dash/')
		except:
			return redirect('/login/')
	context = {
		'form': form
	}
	return render(request,'login.html',context)

def signup(request):
	form = Signup_Form(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		confirm_password= form.cleaned_data.get('confirm_password')
		if password == confirm_password:
			user.set_password(password)
			user.save()
			new_user = authenticate(username=user.username, password=password)
			login(request,new_user)
			return redirect('/dash/')

	form = Signup_Form()

	context = {
		'form':form
	}
	return render(request,'signup.html', context)
	 