from django import forms
from django.db.models import fields

from .models import Company,Toys

# create a ModelForm
class CompanyForm(forms.ModelForm):
	
	class Meta:
		model = Company
		fields = ('company_name','location','email_id')
        

class ToyForm(forms.ModelForm):
    
    class Meta:
        model = Toys
        fields = "__all__"
