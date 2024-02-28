from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about_us'),
    path('contact/', views.ContactPageView.as_view(), name='contact_us'),
    path('services/', views.ServicesPageView.as_view(), name='our_services'),
    path('contact/submit/', views.ContactFormSubmitView.as_view(), name='contact_form_submit')
]
