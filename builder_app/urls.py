from django.urls import path

from . import views

urlpatterns = [
    path('curve/', views.TablesInfoView.as_view()),
]