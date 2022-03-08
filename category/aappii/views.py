from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import *
from .serializer import CtegorySerializer

#all objects in category
@api_view()
def categories(request):
  categories=Category.objects.all()
  serializer= CtegorySerializer(categories, many=True)

  return Response(serializer.data)


  #get single item

def get_single_category(request,pk):
    category = Category.objects.get(pk=pk)
    serializer= CtegorySerializer(category)
    return Response(serializer.data)