from django.urls import path

from . import views
app_name = 'company'
urlpatterns = [
    path('',views.IndexView.as_view(), name='IndexView'),

    path('form/',views.CompanyView.as_view(),name='company'),

    path('show/<int:pk>/',views.CompanyDetailView.as_view(),name='CompanyDetailView'),

    path('update/<int:pk>/',views.CompanyUpdateView.as_view(),name='CompanyUpdateView'),

    path('delete/<int:pk>/',views.CompanyDeleteView.as_view(),name='CompanyDeleteView'),

    path('toy/',views.ToyView.as_view(),name='toy'),

    path('toy/show/<int:pk>/',views.ToyDetailView.as_view()),

    path('toy/update/<int:pk>/',views.ToyUpdateView.as_view()),

    path('toy/delete/<int:pk>/',views.ToyDeleteView.as_view(),name='ToyDeleteView'),
]