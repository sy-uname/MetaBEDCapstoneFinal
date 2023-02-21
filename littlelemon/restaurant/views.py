from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, status, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from restaurant.auth import IsBaseAuthenticated
from restaurant.models import Booking, Menu
from restaurant.serializers import MenuSerializer, BookingSerializer, UserSerializer


def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsBaseAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by('title')
    permission_classes = [IsBaseAuthenticated]
    serializer_class = MenuSerializer
    ordering_fields = [
        'title',
        'price',
        'inventory',
    ]
    filterset_fields = [
        'price',
        'title',
    ]
    search_fields = [
        'price',
        'title',
        'inventory',
    ]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    permission_classes = [IsBaseAuthenticated]
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer