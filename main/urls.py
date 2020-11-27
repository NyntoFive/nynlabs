from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from main import models
from main import views

urlpatterns = [
    path("product/<slug:slug>/", DetailView.as_view(model=models.Product), name="product",),
    path("products/<slug:tag>/", views.ProductListView.as_view(), name="products"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path('about/', TemplateView.as_view(template_name="main/about.html")),
    path('', TemplateView.as_view(template_name="main/home.html")),
]
