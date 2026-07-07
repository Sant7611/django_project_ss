from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProfileSerializer
from .models import Profile

# Create your views here.
@api_view(['POST', 'GET'])
def user(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)