from django.urls import path

from movies import views

urlpatterns = [
    path('list/', views.list),
    path('details/<id>', views.details)
]
