from django.urls import path
from . import views

app_name = 'resources'


urlpatterns = [
    path('', views.resources_list, name="resources_list"),
    path('<slug:slug>/', views.resources_detail, name="detail")
]