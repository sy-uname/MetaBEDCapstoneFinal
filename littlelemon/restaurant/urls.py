from django.urls import path, include
from . import views

app_name = 'restaurant'

menuitems_patterns = (
    [
        path('', views.MenuItemsView.as_view()),
        path('<int:pk>', views.SingleMenuItemView.as_view()),
    ], 'menuitems'
)

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', include(menuitems_patterns)),
]