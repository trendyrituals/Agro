from django.urls import path
from .views import home, login_v,signup
urlpatterns = [
    path('signup/',signup,name='sign_up_url'),
    path('login/',login_v,name='login_url'),
    path('',home,name='home-url')
]