from rest_framework import generics
from transformers.models import Transformer
from transformers.serializer import TransformerSerializer

""" Using generic class-based views """
class TransformerList(generics.ListCreateAPIView):
    queryset = Transformer.objects.all()
    serializer_class = TransformerSerializer

class TransformerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transformer.objects.all()
    serializer_class = TransformerSerializer