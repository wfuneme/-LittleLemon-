from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import MenuViewSet,BookingViewSet,UserViewSet
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet) 

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    
]