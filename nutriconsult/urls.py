from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset-password/complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register-assistant/', views.assistant_register, name='assistant_register'),
    path('register-nutritionist/', views.nutritionist_register, name='nutritionist_register'),
    path('register-client/', views.client_register, name='client_register'),
    path('make-consult/', views.make_consult, name='make_consult'),
    path('patient-detail/<int:client_id>/', views.patient_details, name='patient_detail'),
    path('patient-progress/', views.patient_progress, name='patient_progress'),
]

