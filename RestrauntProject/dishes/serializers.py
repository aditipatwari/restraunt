from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class Dishes_serializers(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom fields from the user model to the token response
        data.update({
            'age':self.user.age,
            'is_verified':self.user.is_verified
            # add more fields as needed
        })
        
        return data
