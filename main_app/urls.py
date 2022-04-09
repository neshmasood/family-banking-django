from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name="landing_page"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('tasks/', views.TaskList.as_view(), name="task_list"),
  

]