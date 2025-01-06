from django.urls import path

from movies import views

urlpatterns = [
    path('', views.catalog),
    path('list/', views.list),
    path('details/<id>', views.details),
    path('create', views.create),
    path('edit/<id>', views.edit),
    path('delete/<id>', views.delete)
]