from . models import Menu, Booking
from . serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
     
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  
    serializer_class = BookingSerializer  
    permission_classes = [IsAuthenticated]
  
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    