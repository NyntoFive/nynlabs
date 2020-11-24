from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path("contact/", views.ContactView.as_view(), name="contact"),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('', TemplateView.as_view(template_name="home.html")),
]
