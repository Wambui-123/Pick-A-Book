from dataclasses import fields
from rest_framework import serializers
from .models import Books,Profile, Category,Cart,Delivery
from django.contrib.auth.models import User



class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model=Books
        fields = '__all__'

        
class PostBookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

    class Meta:
        model=Books
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True,many=True)
    class Meta:
        model = Cart
        fields = '__all__'  

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('order','user','delivery_status')
