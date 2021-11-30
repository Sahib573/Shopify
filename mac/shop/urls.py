from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('products/<int:myid>/', views.products, name="products"),
    path('complaint/', views.complaint, name="complaint"),
    path('tracker/', views.tracker, name="tracker")
]
