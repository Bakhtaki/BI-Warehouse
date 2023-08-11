from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views

# app_name = 'complaint'

urlpatterns = [
    path('-js-catalog',
         JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
]
