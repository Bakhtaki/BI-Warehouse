from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from .forms import Create_ComplaintForm


class ComplaintView(FormView):
    template_name = 'complaints.html'
    form_class = Create_ComplaintForm
    success_url = '/'

    def form_valid(self, form):
        return super(ComplaintView, form).form_valid(form)


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, template_name='landing.html')