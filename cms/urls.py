from django.urls import path, re_path
from cms import views

app_name = "cms"

urlpatterns = [
    # This pattern matches the home page (e.g., yoursite.com/)
    path('', views.home, name='home'),
    
    # This pattern matches any other URL and passes the path as 'permalink'
    # The 're_path' is used for regular expression matching.
    re_path(r'^(?P<permalink>.+)/$', views.home, name='permalink'),
]