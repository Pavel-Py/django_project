from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from jum.forms import ResumeForm, ResumeEditForm
from jum.mixins import ForUserWithoutResumeMixin, ForUserWithResumeMixin
from jum.models import Resume


class ResumeStartView(TemplateView):
    template_name = 'jum/resume/start.html'


class ResumeCreateView(ForUserWithoutResumeMixin, CreateView):
    template_name = 'jum/resume/create.html'
    form_class = ResumeForm
    model = Resume

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = User.objects.get(id=self.request.user.id)
        instance.save()
        return redirect('resume')


class ResumeUpdateView(LoginRequiredMixin, ForUserWithResumeMixin, UpdateView):
    template_name = 'jum/resume/create.html'
    form_class = ResumeEditForm
    model = Resume
    success_url = reverse_lazy('resume')

    def get_object(self, queryset=None):
        return Resume.objects.get(user_id=self.request.user.id)
