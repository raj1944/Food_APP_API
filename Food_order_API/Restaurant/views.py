from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .serializers import RestaurantsSerializer, BranchesSerializer, FoodSerializer, MenuSerializer
from .serializers import OrderSerializer, orderItemSerializer, UserSerializer
from .models import Restaurants, Branches, Food, Menu, Order, orderItem, User
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status


class UserViewSet(APIView):

    def get(self, request, id=None, *args, **kwargs):
        if id != None:
            user = User.objects.filter(id=id)
        else:    
            user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantViewSet(APIView):

    def get(self, request, id=None, *args, **kwargs):
        if id != None:
            restaurant = Restaurants.objects.filter(id=id)
        else:    
            restaurant = Restaurants.objects.all()
        serializer = RestaurantsSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RestaurantsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchViewSet(APIView):

    def get(self, request, id=None, *args, **kwargs):
        if id != None:
            branch = Branches.objects.filter(id=id)
        else:
            branch = Branches.objects.all()
        serializer = BranchesSerializer(branch, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BranchesSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodViewSet(APIView):

    def get(self, request, id=None, *args, **kwargs):
        if id != None:
            food = Food.objects.filter(id=id)
        else:
            food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FoodSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuViewSet(APIView):

    def get(self, request, id=None, *args, **kwargs):
        if id != None:
            menu = Menu.objects.filter(id=id)
        else:    
            menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id=None, *args, **kwargs):
        if id != None:
            menu = Menu.objects.get(id=id)
            serializer = MenuSerializer(instance=menu, data=request.data)
        else:    
            serializer = MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(APIView):

    def get(self, request, id=None, *args, **kwargs):
        if id != None:
            order = Order.objects.filter(id=id)
        else:    
            order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id=None, *args, **kwargs):
        if id != None:
            return Response({"message" : "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)    
        order_data = {}
        order_data['delivery_addr'] = request.data['delivery_addr']
        order_data['user_id'] = request.data['user_id']
        order_data['branch_id'] = request.data['branch_id']
        order_data['total_amount'] = 0

        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            order_id = order_serializer.data['id']
            order_food = request.data['order_food']
            total_amount = 0
            items = []
            for x, y in order_food:
                menu = Menu.objects.filter(id=x)
                item = []
                if menu[0].quantity < y:
                    order = Order.objects.get(id=order_id)
                    order.delete()
                    return Response({"message":"Sorry not able to place your order"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    temp_menu = Menu.objects.get(id=x)
                    temp_menu.quantity = menu[0].quantity - y
                    temp_menu.save()

                temp_data = {}
                temp_data['menu_id'] = menu[0].id
                temp_data['order_id'] = order_id
                temp_data['quantity'] = y
                temp_data['total_price'] = y * menu[0].price
                
                total_amount += temp_data['total_price']
                item.append(menu[0].food.food_name)
                item.append(y)
                item.append(temp_data['total_price'])

                orderitem_serializer = orderItemSerializer(data=temp_data)
                if orderitem_serializer.is_valid():
                    orderitem_serializer.save()
                else:
                    order = Order.objects.get(id=order_id)
                    order.delete()
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                items.append(item)
            
            order = Order.objects.get(id=order_id)
            order_data['total_amount'] = total_amount
            serializer = OrderSerializer(instance=order, data=order_data)
            if serializer.is_valid():
                serializer.save()
            else:
                order = Order.objects.get(id=order_id)
                order.delete()
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            response_data = {
                "order_id" : order_id,
                "total_amount" : total_amount,
                "items" : items 
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        order = Order.objects.get(id=order_id)
        order.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render

# Create your views here.
