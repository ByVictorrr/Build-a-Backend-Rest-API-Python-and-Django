from rest_framework import serializers



class HelloSerializer(serializers.Serializer):
    """Serializes a name field for test our APIView"""
    # below is the variable that we get on the page for an form input
    name = serializers.CharField(max_length=10)

