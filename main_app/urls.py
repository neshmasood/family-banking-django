from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name="landing_page"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.signup_view, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('tasks/', views.TaskList.as_view(), name="task_list"),
    path('tasks/new/', views.TaskCreate.as_view(), name="task_create"),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name="task_detail"),
    path('tasks/<int:pk>/update', views.TaskUpdate.as_view(), name="task_update"),
    path('tasks/<int:pk>/delete', views.TaskDelete.as_view(), name="task_delete"),
    # path('familygroups/', views.familygroup_index, name='familygroups_index'),
    # path('familygroups/<int:familygroup_id>', views.familygroup_show, name='familygroups_show'),
    # path('familygroups/create/', views.FamilyGroupCreate.as_view(), name='familygroups_create'),
    # path('familygroups/<int:pk>/update/', views.FamilyGroupUpdate.as_view(), name='familygroups_update'),
    # path('familygroups/<int:pk>/delete/', views.FamilyGroupDelete.as_view(), name='familygroups_delete'),
 

]