from django.db.models import fields
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . models import *

class CategorySerializer(ModelSerializer):
    random_photo = SerializerMethodField()
    
    def get_random_photo(self , obj):
        try:
            return obj.products.first().photo
        except:
            return ""
        
    class Meta:
        model = Category
        fields=(
            'id' , 'name' , 'random_photo'
        )
        
class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields=(
            "id" , "name"
        )
        
class ProductsAllInfoSerializer(ModelSerializer):
    category = CategorySerializer()
    seller =SellerSerializer()
    class Meta:
        model =Product
        fields=(
            'id', 'photo','price','title','category','seller','photo'
            )



class ProductSerializer(ModelSerializer):
    class Meta:
        model =Product
        fields=(
            'id', 'photo','price','title','category','seller','photo'
        )
    