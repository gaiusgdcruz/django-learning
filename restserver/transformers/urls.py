from django.urls import path
from transformers import views


urlpatterns = [
    path('transformers/',
         views.transformer_list),
    path('transformers/<int:pk>/',
         views.transformer_detail),
]