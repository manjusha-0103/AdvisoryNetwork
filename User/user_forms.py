from django import forms
#from django.forms import EmailInput, PasswordInput

from .models import Register

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

#from login.core.forms import django
'''
def signup(request):
    if request.method == 'POST':
        form = django(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = django()
    return render(request, 'signup.html', {'form': form})'''
'''
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password", "note_time")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
'''