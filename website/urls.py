from django.urls import path
from . import views
# from views import home


urlpatterns = [
    # path('', home, name='home'),
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('table/', views.table, name='table'),
]