from django.contrib import admin

# Register your models here.
from .models import Register

#class RegisterAdmin(Advisor.ModelAdmin):
 #   fields = ['form.username','email','form.password',]

admin.site.register(Register)#,RegisterAdmin)
