from django.urls import path

from .views import SigninView, SignoutView, SignupView

urlpatterns = [
    path('signin/', SigninView.as_view(), name= "signin"),
    path('signout/', SignoutView.as_view(), name= 'signout'),
    path('signup/', SignupView.as_view(), name= 'signup'),
]
