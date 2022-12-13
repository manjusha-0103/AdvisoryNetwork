
# Register your models here.

from django import forms
from .models import Advisor_info

class Advisorform(forms.ModelForm):
    class Meta:
        model = Advisor_info
        fields = ("name","photo","note_time",)

