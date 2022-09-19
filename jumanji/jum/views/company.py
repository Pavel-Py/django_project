from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from jum.forms import CompanyForm
from jum.mixins import ForUserWithoutCompany, ForUserWithCompanyMixin
from jum.models import Company


class CompanyStartView(ForUserWithoutCompany, TemplateView):
    template_name = 'jum/company/start.html'


class CompanyCreateView(ForUserWithoutCompany, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'jum/company/create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return redirect('company-edit')


class CompanyEditView(ForUserWithCompanyMixin, UpdateView):
    model = Company
    template_name = 'jum/company/edit.html'
    form_class = CompanyForm
    success_url = reverse_lazy('company-edit')

    def get_object(self, queryset=None):
        return Company.objects.get(owner=self.request.user.id)
