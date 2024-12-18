from django.urls import path

from movies import views

urlpatterns = [
    path('', views.list),
    path('details/<id>', views.details),
    path('create', views.create),
    path('delete/<id>', views.delete)
]