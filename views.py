import company
from company.models import Company, Toys
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from .forms import CompanyForm,ToyForm
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'company/index.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['toy_list']= Toys.objects.all()
        return context


class CompanyView(generic.FormView):
    form_class = CompanyForm
    template_name = 'company/company.html'
    
    success_url = '/company'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ToyView(generic.FormView):
    form_class = ToyForm
    template_name = 'company/toy.html'

    success_url = '/company'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class CompanyUpdateView(generic.UpdateView):
    model = Company
    fields = ['company_name','location','email_id']
    success_url = '/company'
    def exist(company, company_id):
        pk=company_id
        

class CompanyDetailView(generic.DetailView):
    model = Company
    fields = '__all__'




