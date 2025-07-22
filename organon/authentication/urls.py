from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/', LogoutView.as_view(next_page='authentication:login'), name='logout'),
]
