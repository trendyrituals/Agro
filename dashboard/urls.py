from django.urls import path
from .views import home,logout_v,sales_hub,marketing_hub,customer_support
urlpatterns = [
	path('sales/',sales_hub,name='sales_url'),
	path('marketing/',marketing_hub,name='marketing_url'),
	path('customer/',customer_support,name='customer_url'),
	path('logout/',logout_v,name='logout_url'),
    path('',home,name='home-url')
]