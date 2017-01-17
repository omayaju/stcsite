from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from accounts import views

urlpatterns = [
    url(r'^login/$',  views.login, name = 'login'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^register/$', views.RegisterFormView.as_view(), name = 'register'),
] 
