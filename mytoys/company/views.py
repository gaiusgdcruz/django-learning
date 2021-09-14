
from company.models import Company, Toys
from django.urls import reverse, reverse_lazy
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
    
    

class CompanyView(generic.CreateView):
    model = Company
    template_name = 'company/company.html'
    fields = '__all__'
    success_url = '/company'


class CompanyDetailView(generic.DetailView):
    model = Company
    fields = '__all__'

class CompanyUpdateView(generic.UpdateView):
    model = Company
    fields = '__all__'
    success_url = '/company'

class CompanyDeleteView(generic.DeleteView):
    model = Company
    fields = '__all__'
    success_url = '/company'

class ToyView(generic.CreateView):
    model = Toys
    fields = '__all__'
    template_name = 'toys/toy.html'
    success_url = '/company'

class ToyDetailView(generic.DetailView):
    model = Toys
    fields = '__all__'
    template_name = 'toys/toy_detail.html'
    

class ToyUpdateView(generic.UpdateView):
    model = Toys
    fields = '__all__'
    template_name = 'toys/toy_form.html'
    success_url = '/company'

class ToyDeleteView(generic.DeleteView):
    model = Toys
    fields = '__all__'
    template_name = 'toys/toy_confirm_delete.html'
    success_url = '/company'

