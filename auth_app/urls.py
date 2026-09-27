from django.urls import path
from auth_app.views import*

urlpatterns = [
    path('', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('logout,', logout_view, name='logout_view'),

]