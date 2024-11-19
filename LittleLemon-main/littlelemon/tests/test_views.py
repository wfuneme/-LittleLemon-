from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer  
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        Menu.objects.create(title="Pizza", price=10.99, inventory=15)
        Menu.objects.create(title="Pasta", price=8.99, inventory=30)
        Menu.objects.create(title="Salad", price=5.99, inventory=10)

    def test_getall(self):
        response = self.client.get(reverse('menu-list')) 
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
