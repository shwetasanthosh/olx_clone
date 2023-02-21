from django.contrib import admin
from django.urls import path
from buyer import views

urlpatterns=[
    path("admin/",admin.site.urls),
    path("register",views.SignUpView.as_view(),name="register"),
    path("home",views.HomeView.as_view(),name="home"),
    path("userprofile",views.UserProfileView.as_view(),name="userprofile"),
    path("",views.SignInView.as_view(),name="signin"),
    
]   