from django.shortcuts import render, redirect
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	)
# Create your views here.

def home(request):
	# print(request.user.username)
	if request.user.is_authenticated:
		user = request.user.username
		context = {
			'username': user
		}
		return render(request,'dash.html',context)
	else:
		return redirect('/login/')

def marketing_hub(request):
	# print(request.user.username)
	if request.user.is_authenticated:
		user = request.user.username
		context = {
			'username': user
		}
		return render(request,'marketing.html',context)
	else:
		return redirect('/login/')


def sales_hub(request):
	# print(request.user.username)
	if request.user.is_authenticated:
		user = request.user.username
		context = {
			'username': user
		}
		return render(request,'sales.html',context)
	else:
		return redirect('/login/')



def customer_support(request):
	# print(request.user.username)
	if request.user.is_authenticated:
		user = request.user.username
		context = {
			'username': user
		}
		return render(request,'customer.html',context)
	else:
		return redirect('/login/')



def logout_v(request):
	logout(request)
	return redirect('/')