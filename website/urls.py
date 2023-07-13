from django.urls import path
from . import views
# from views import home


urlpatterns = [
    # path('', home, name='home'),
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    path(r'form', views.my_form, name='form')
]