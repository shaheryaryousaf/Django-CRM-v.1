from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

# ===============================
# User Creation Form
# ===============================
class UserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name' , 'email', 'password1', 'password2', 'is_staff')
        widgets = {
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.fields.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.fields.TextInput(attrs={'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
        unique_together = ('email',)

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


# ===============================
# Agent Creation Form
# ===============================
class AgentCreationForm(UserCreationForm):
    class Meta:
        model = User
        # exclude = ('password1', 'password2', 'is_staff')
        fields = ('first_name', 'last_name' , 'email', 'password1')
        unique_together = ('email',)

    def __init__(self, *args, **kwargs):
        super(AgentCreationForm, self).__init__(*args, **kwargs)
        # del self.fields['password1']
        # del self.fields['password2']