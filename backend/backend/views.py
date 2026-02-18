from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from django.contrib.auth.models import User
from .models import Job
from .serializers import JobSerializer

@api_view(['GET'])
def test_api(request):
    return Response({"message" : "you did it!"})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered Successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username, password=password)
        return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def jobs_list(request):
    jobs = Job.objects.all()
    serializers = JobSerializer(jobs, many=True)
    return Response(serializers.data)