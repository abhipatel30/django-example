from patel import views
from django.conf.urls import url

app_name = 'patel'

urlpatterns = [
            url('register/', views.register, name='register'),
            url('login/', views.user_login, name='user_login'),
]
