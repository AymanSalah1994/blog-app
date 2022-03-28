import imp
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    # Inherit From CreateView So That , it is a Creation Process 
    form_class = UserCreationForm
    #  This is T send a "Form Context processor" to our template ,
    # Form == Model & Vice Versa , If we Use a Pre-Build Form , this means There are Corresponding Model Fields  ; 
    success_url = reverse_lazy('login')
    # ???
    template_name = 'registration/signup.html'
