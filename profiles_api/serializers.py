from rest_framework import serializers
from profiles_api import models



class HelloSerializer(serializers.Serializer):
    """Serializes a name field for test our APIView"""
    # below is the variable that we get on the page for an form input
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # needed for a modelSerialier
    # also makes it so the fields show on the html form
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
                'password':{
                    'write_only': True,
                    'style': {"input_type": "password"}
                    }
                }


    #over ride the creat function in ModelSerializer
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password']
                )
        return user



