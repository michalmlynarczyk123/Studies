from django.urls import path
from . import views

urlpatterns = [
    path('hello-world', views.hello_world),
    path('current-date', views.current_date),
    path('view-hits', views.view_hits),
    path('country/<int:country_index>', views.find_country_by_index),
    path('country/<str:country_name>', views.find_country_by_name, name='country_by_name_url'),
    path('first-html', views.first_html, name='first_html_url'),
    path('first-template', views.first_template, name='first_template_url')
]
