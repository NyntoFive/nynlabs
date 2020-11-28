from django.contrib.auth import views as auth_views
from main import forms

from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from main import models
from main import views

urlpatterns = [
    path("login/", 
         auth_views.LoginView.as_view(
             template_name="main/login.html",
             form_class=forms.AuthenticationForm,
            ),
        name="login",
        ),
    path('signup/', views.SignUpView.as_view(), name="signup"),

    path(
        "address/",
        views.AddressListView.as_view(),
        name="address_list",
    ),
    path(
        "address/create/",
        views.AddressCreateView.as_view(),
        name="address_create",
    ),
    path(
        "address/<int:pk>/",
        views.AddressUpdateView.as_view(),
        name="address_update",
    ),
    path(
        "address/<int:pk>/delete/",
        views.AddressDeleteView.as_view(),
        name="address_delete",
    ),
    path(
        "add_to_basket/",
        views.add_to_basket,
        name="add_to_basket",
    ),
    path('basket/', views.manage_basket, name="basket"),
    path(
        "order/done/",
        TemplateView.as_view(template_name="order_done.html"),
        name="checkout_done",
        ),
    path(
        "order/address_select/",
        views.AddressSelectionView.as_view(),
        name="address_select",
        ),

    path("product/<slug:slug>/", DetailView.as_view(model=models.Product), name="product",),
    path("products/<slug:tag>/", views.ProductListView.as_view(), name="products"),
    path('dev/', TemplateView.as_view(template_name="dev.html")),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path('about/', TemplateView.as_view(template_name="main/about.html")),
    path('', TemplateView.as_view(template_name="main/home.html"), name="home"),
]
