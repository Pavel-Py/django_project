from django.db.models import Count, Q
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from jum.forms import ApplicationForm
from jum.models import Specialty, Company, Vacancy, Application


class MainView(TemplateView):
    template_name = 'jum/main/index.html'
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialities'] = Specialty.objects.all().annotate(Count('vacancies'))
        context['companies'] = Company.objects.all().annotate(Count('vacancies'))
        return context


class CompanyView(DetailView):
    model = Company
    template_name = 'jum/main/company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(company__pk=self.kwargs['pk'])
        return context


class VacanciesByCatView(ListView):
    model = Vacancy
    template_name = 'jum/main/vacancies.html'

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialty'] = get_object_or_404(Specialty, code=self.kwargs['slug'])
        return context


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'jum/main/vacancies.html'
    context_object_name = 'vacancies'


class SearchView(ListView):
    template_name = 'jum/main/vacancies.html'

    def get_queryset(self):
        """
        Фильтрует вакансии по наличию любого слова из поиска в полях description или title.
        Возвращает QuerySet
        """
        words = [word for word in self.request.GET.get('s').split(' ')]
        list_objects = Vacancy.objects.filter(Q(description__icontains=words[0]) | Q(title__icontains=words[0]))
        for word in words[1:]:
            list_objects = list_objects.filter(Q(description__icontains=word) | Q(title__icontains=word))
        return list_objects


class VacancyView(CreateView):
    model = Application
    template_name = 'jum/main/vacancy.html'
    form_class = ApplicationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.vacancy = Vacancy.objects.get(id=self.kwargs['pk'])
        form.save()
        return redirect('all_vacancies')

    def get_context_data(self, **kwargs):
        context = super(VacancyView, self).get_context_data(**kwargs)
        context['vacancy'] = get_object_or_404(Vacancy, id=self.kwargs['pk'])
        return context




def custom_handler404(request, exceptions):
    return HttpResponseNotFound('Страница не найдена, ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
