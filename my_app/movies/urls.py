from django.urls import path

from movies import views

urlpatterns = [
    path('', views.list),
    path('details/<id>', views.details),
    path('delete/<id>', views.delete)
]