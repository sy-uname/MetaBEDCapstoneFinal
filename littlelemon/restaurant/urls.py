from django.contrib import admin 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash = True)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='index'),
    path('api/menu/items/', views.MenuItemsView.as_view()),
    path('api/menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('restaurant/booking/', include(router.urls)),
]

