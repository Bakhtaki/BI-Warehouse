from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import Create_ComplaintForm
import jdatetime


class ComplaintView(FormView):
    template_name = 'complaints.html'
    form_class = Create_ComplaintForm
    success_url = '/'

    def form_valid(self, form):
        return super(ComplaintView, form).form_valid(form)


def complaint_list(request):
    return HttpResponse(jdatetime.datetime.today().strftime("%Y/%m/%d"))
