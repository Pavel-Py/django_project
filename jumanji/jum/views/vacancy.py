from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from jum.forms import VacancyForm, VacancyEditForm
from jum.models import Vacancy, Company, Application
from jum.mixins import ForUserWithCompanyMixin


class UserVacancyView(ForUserWithCompanyMixin, ListView):
    model = Vacancy
    template_name = 'jum/vacancy/main.html'

    def get_queryset(self):
        return self.request.user.company.vacancies.all()


class VacancyCreteView(ForUserWithCompanyMixin, CreateView):
    model = Vacancy
    template_name = 'jum/vacancy/create.html'
    form_class = VacancyForm

    def form_valid(self, form):
        form.instance.company = Company.objects.get(owner=self.request.user.id)
        form.save()
        return redirect('user-vacancy')


class VacancyEditView(ForUserWithCompanyMixin, UpdateView):
    model = Vacancy
    template_name = 'jum/vacancy/edit.html'
    form_class = VacancyEditForm
    success_url = reverse_lazy('user-vacancy')

    def get_object(self, queryset=None):
        return Vacancy.objects.get(id=self.kwargs['pk'])


class ApplicationsView(ForUserWithCompanyMixin, ListView):
    model = Application
    template_name = 'jum/vacancy/applications.html'

    def get_queryset(self):
        return Application.objects.filter(vacancy_id=self.kwargs['pk'])
