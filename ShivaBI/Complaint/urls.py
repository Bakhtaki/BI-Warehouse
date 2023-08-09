from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path(
        '-js-catalog', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('complaint', views.ComplaintView.as_view(), name='complaint'),
]
