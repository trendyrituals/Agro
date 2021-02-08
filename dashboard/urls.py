from django.urls import path
from .views import home,logout_v
urlpatterns = [
	path('logout/',logout_v,name='logout_url'),
    path('',home,name='home-url')
]