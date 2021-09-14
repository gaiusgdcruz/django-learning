from django import forms
from django.db.models import fields

from .models import Company,Toy

# create a ModelForm
class CompanyForm(forms.ModelForm):
	
	class Meta:
		model = Company
		fields = "__all__"

class ToyForm(forms.ModelForm):
    
    class Meta:
        model = Toy
        fields = "__all__"
