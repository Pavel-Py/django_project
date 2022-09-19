from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View


class BaseForUserWithCompanyMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'company'):
            return redirect('company-start')
        return super().dispatch(request, *args, **kwargs)


class ForUserWithCompanyMixin(LoginRequiredMixin, BaseForUserWithCompanyMixin):
    pass


class BaseForUserWithoutCompany(View):
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'company'):
            return redirect('company-edit')
        return super().dispatch(request, *args, **kwargs)


class ForUserWithoutCompany(LoginRequiredMixin, BaseForUserWithoutCompany):
    pass


class ForUserWithResumeMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'resume'):
            return super().dispatch(request, *args, **kwargs)
        return redirect('resume-start')


class ForUserWithoutResumeMixin(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'resume'):
            return redirect('resume')
        return super().dispatch(request, *args, **kwargs)
