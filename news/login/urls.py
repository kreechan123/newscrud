from django.urls import path
from . import views #see app named login then views file
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.indexView, name='index'), # '' is the path to access views.py function named indexView
    path('dashboard/',views.dashboardView, name="dashboard"), 
    path('login/',LoginView.as_view(), name="login_url"),
    path('register/',views.registerView, name="register_url"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('add/',views.addView, name="add"),
    path('<int:id>/edit', views.editView, name='edit'),
    path('<int:id>/delete', views.deleteView, name='delete'),
    path('<int:id>/', views.deleteView, name='delete'),
]