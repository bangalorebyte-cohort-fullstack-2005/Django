from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form , name ="employee_form"),
    path('list/', views.employee_list, name="employee_list"),
    path("<int:id>/",views.employee_form, name = "employee_update"),
]