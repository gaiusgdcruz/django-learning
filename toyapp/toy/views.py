from django.shortcuts import render
from toy.models import Company,Toy
from .forms import CompanyForm,ToyForm
from django.http import HttpResponse, HttpResponseRedirect





# Create your views here.
def index(request):
    company_list = Company.objects.order_by('comp_name')[:5]
    toy_list = Toy.objects.order_by('toy_name')[:5]
    cform = CompanyForm()
    tform = ToyForm()

    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/toys')
    
    form_b = ToyForm(request.POST or None)
    if form_b.is_valid():
        form_b.save()
        return HttpResponseRedirect('/toys')

    context = {
        'company_list': company_list,
        'toy_list': toy_list,
        'cform':cform, 
        'tform':tform
        }

    return render(request, 'toy/index.html',context)

 

    
