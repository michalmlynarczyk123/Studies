from django.urls import path
from . import views

urlpatterns = [
    path('hello-world', views.hello_world),
    path('current-date', views.current_date),
    path('view-hits', views.view_hits),
    path('country/<country_name>', views.find_country_by_name)
]
