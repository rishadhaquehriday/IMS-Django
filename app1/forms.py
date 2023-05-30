# from django import forms


# class EmployeeForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


from django.forms import ModelForm
from .models import Employee
from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True)
        }
    