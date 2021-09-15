from django.urls import path
from transformers import views

urlpatterns = [
    path('transformers/', views.TransformerList.as_view()),
    path('transformers/<int:pk>/', views.TransformerDetail.as_view()),
]

