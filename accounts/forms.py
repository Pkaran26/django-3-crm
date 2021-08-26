from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control',}
        self.fields['email'].widget.attrs = {'class': 'form-control',}
        self.fields['password1'].widget.attrs = {'class': 'form-control',}
        self.fields['password2'].widget.attrs = {'class': 'form-control',}

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control',}
        self.fields['password1'].widget.attrs = {'class': 'form-control',}

    class Meta:
        model = User
        fields = ['username', 'password1']
