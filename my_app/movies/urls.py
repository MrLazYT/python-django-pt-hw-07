from django.urls import path

from movies import views

urlpatterns = [
    path('', views.catalog),
    path('list/', views.list),
    path('details/<id>', views.details),
    path('create', views.create),
    path('edit/<id>', views.edit),
    path('delete/<id>', views.delete),
    path('favorites/', views.favorites),
    path('add-to-favorites/<movie_id>', views.add_to_favorites_view),
    path('remove-from-favorites/<movie_id>', views.remove_from_favorites_view),
    path('clear-favorites/', views.clear_favorites_view),
]