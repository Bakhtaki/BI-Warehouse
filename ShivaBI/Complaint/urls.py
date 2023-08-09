from django.urls import path
from django.views.i18n import JavaScriptCatalog
from Complaint.views import ComplaintView, LandingPageView

app_name = 'complaint'

urlpatterns = [
    path('', LandingPageView.as_view(), name='complaint'),
    path('complaint/', ComplaintView.as_view(), name='complaint'),
    path('-js-catalog',
         JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
