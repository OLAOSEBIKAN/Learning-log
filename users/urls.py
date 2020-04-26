from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import log_out, register


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),

]
