from django.urls import path
from .import views
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = 'account'

urlpatterns = [
    # API
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('profile', views.UserView.as_view(),name='profile_view'),


# =========================================================================

    path('loginn', views.UserLogin.as_view(), name='user_login'),
    path('otplogin', views.RegisterView.as_view(), name='register'),
    path('checkotp', views.CheckOtpView.as_view(), name='check_otp'),
    path('logout', views.user_logout, name='logout'),
    path('add/address', views.AddAddressView.as_view(), name='add_address'),

]