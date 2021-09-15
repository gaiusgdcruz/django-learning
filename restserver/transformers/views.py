from django.shortcuts import render
from django.http import Http404, response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from transformers.models import Transformer
from transformers.serializer import TransformerSerializer

# Create your views here.

@api_view(['GET','POST'])
def transformerlist(request):

    if request.method == 'GET':
        transformer = Transformer.objects.all()
        serializer = TransformerSerializer(transformer, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TransformerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def transformerdetail(request, pk):
    try:
        transformer = Transformer.objects.get(pk=pk)
    except Transformer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TransformerSerializer(transformer)
        return(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TransformerSerializer(transformer,data=request.data)
        
        if serializer. is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = TransformerSerializer(transformer,data=request.data,partial=True)

        if serializer. is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)