from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('products/<int:myid>/', views.products, name="products"),
    path('complaint/', views.complaint, name="complaint"),
    path('tracker/', views.tracker, name="tracker"),
    path('cancel/', views.cancel, name="cancel"),
    path('cancelorder/', views.cancelorder, name="cancelorder"),
    path('replace/', views.replace, name="replace"),
    path('replaceorder/', views.replaceorder, name="replaceorder"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name="logout"),
    path('profile/', views.profile, name="profile")
]
