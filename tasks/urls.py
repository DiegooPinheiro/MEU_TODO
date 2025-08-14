from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('create/', views.task_create, name='create'),
    path('edit/<int:pk>/', views.task_edit, name='edit'),
    path('delete/<int:pk>/', views.task_delete, name='delete'),
    path('toggle/<int:pk>/', views.task_toggle, name='toggle'),

    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='tasks:login'), name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
]

