from django.urls import path

from jum.views.company import CompanyEditView, CompanyCreateView, CompanyStartView
from jum.views.main import AllVacanciesView, CompanyView, VacanciesByCatView, SearchView, VacancyView
from jum.views.resume import ResumeUpdateView, ResumeCreateView, ResumeStartView
from jum.views.vacancy import UserVacancyView, VacancyCreteView, VacancyEditView, ApplicationsView

urlpatterns = [
    path('vacancies/', AllVacanciesView.as_view(), name='all_vacancies'),
    path('vacancy/<pk>/', VacancyView.as_view(), name='vacancy'),
    path('company/<pk>/', CompanyView.as_view(), name='company'),
    path('vacancies/cat/<slug>/', VacanciesByCatView.as_view(), name='cat_vacancies'),
    path('company-edit/', CompanyEditView.as_view(), name='company-edit'),
    path('company-create/', CompanyCreateView.as_view(), name='company-create'),
    path('company-start/', CompanyStartView.as_view(), name='company-start'),
    path('user-vacancy/', UserVacancyView.as_view(), name='user-vacancy'),
    path('vacancy-create/', VacancyCreteView.as_view(), name='vacancy-create'),
    path('vacancy-edit/<pk>/', VacancyEditView.as_view(), name='vacancy-edit'),
    path('applications/<pk>/', ApplicationsView.as_view(), name='applications'),
    path('search/', SearchView.as_view(), name='search'),
    path('resume-start/', ResumeStartView.as_view(), name='resume-start'),
    path('resume-create/', ResumeCreateView.as_view(), name='resume-create'),
    path('resume/', ResumeUpdateView.as_view(), name='resume'),
]
