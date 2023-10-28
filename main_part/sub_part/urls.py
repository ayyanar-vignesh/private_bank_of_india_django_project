from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login_page',views.login_page,name='login_page'),
    path('register_page',views.register_page,name='register_page'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),
    path('deposit_form_submission/<str:logger_account_number>',views.deposit_form_submission,name='deposit_form_submission'),
    path('withdraw_form_submission/<str:logger_account_number>',views.withdraw_form_submission,name='withdraw_form_submission'),

]