from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Product
from django.http import HttpResponse
import json
# Create your views here.

@api_view(['GET'])
def test(request):
    return Response({'message': 'hello world'})

def show(request):
    products= Product.objects.all()
    
    lists = {product.__dict__ for product in products}
    json_lst = json.dumps(lists)
    return HttpResponse(json_lst)