from django.contrib import admin
from django.urls import path
from buyer import views

urlpatterns=[
    path("admin/",admin.site.urls),
    path("register",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home",views.HomeView.as_view(),name="home"),
    path("productadd", views.product_create, name="add-product"),
    path("products/details/<int:id>", views.ProductDetailView.as_view(), name="product-detail"),
    path('profile', views.profile_create, name='profile-edit'),
    path('viewprofile',views.ViewProfile.as_view(),name="profile-view"),
    path("myproducts", views.MyProductView.as_view(), name="my-product"),
    path("profile/signout", views.logout_view, name="signout"),
    
]   