from django.urls import path
from transformers import views


urlpatterns = [
    path('transformers/',
         views.transformerlist),
    path('transformers/<int:pk>/',
         views.transformerdetail),
]