from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,TemplateView,DetailView
from django.urls import reverse_lazy
from buyer.forms import RegistrationForm,LoginForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from buyer.models import Products,UserProfile
from django.contrib.auth.models import User
from django.contrib import messages

class HomeView(ListView):
    template_name="index.html"
    context_object_name="products"
    model=Products

class SignUpView(CreateView):
    template_name="signup.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("register")

    def form_valid(self,form):
        messages.success(self.request,"Account Created Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"Account Creation Failed")
        return super().form_invalid(form)

class SignInView(FormView):
    template_name ="login.html"
    form_class = LoginForm

    def post(self, request,args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr=authenticate(request, username = uname, password = pwd)
            if usr: 
                login(request,usr)
                messages.success(request, "Logined Successfully")
                return redirect("home")
            else:
                messages.error(self.request,"Invalid Credentials")     
                return render(request,"login.html",{"form":form})   

class UserProfileView(FormView):
    template_name="user-profile.html"
    form_class=UserCreationForm
    success_url=reverse_lazy

    def form_valid(self, form):
        messages.success(self.request,"Profile Created Successfully")
        return super().form_valid(form)                



                


