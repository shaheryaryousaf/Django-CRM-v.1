from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('signin', auth_views.LoginView.as_view(
         redirect_authenticated_user=True), name='signin'),
    path("logout", LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('agents', views.agents_list, name="agents-list"),
    path('agents/create', views.create_agent, name="create-agent"),
    path('agents/assign/<str:id>', views.assign_agent, name="assign-agent"),
    path('leads/create', views.create_lead, name="create-lead"),
    path('leads/edit/<str:id>', views.edit_lead, name="edit-lead"),
]
