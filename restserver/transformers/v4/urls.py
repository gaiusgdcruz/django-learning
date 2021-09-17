from django.urls import path
from transformers.v2 import views

urlpatterns = [
    path('transformers/', views.TransformerList.as_view()),
    path('transformers/<int:pk>/', views.TransformerDetail.as_view()),
]