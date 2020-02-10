from django.urls import path
from news import views #see app named login then views file

urlpatterns = [
    path('', views.listView, name='list'), # '' is the path to access views.py function named indexView
    # path('dashboard/',views.dashboardView, name="dashboard"), 
    # path('login/',LoginView.as_view(), name="login_url"),
    # path('register/',views.registerView, name="register_url"),
    # path('logout/',LogoutView.as_view(), name="logout")
]