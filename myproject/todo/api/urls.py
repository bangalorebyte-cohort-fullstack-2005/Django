from django.urls import path
from todo.api.views import api_detail_view , api_update_view,api_delete_view,api_create_view

urlpatterns = [
    path('<int:id>',api_detail_view, name='detail'),
    path('update/<int:id>',api_update_view, name="update" ),
    path('delete/<int:id>',api_delete_view, name="delete"),
    path('create',api_create_view, name="create")
]