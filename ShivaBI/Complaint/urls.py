from django.urls import path
from . import views

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('complaint', views.ComplaintView.as_view(), name='complaint'),
]
