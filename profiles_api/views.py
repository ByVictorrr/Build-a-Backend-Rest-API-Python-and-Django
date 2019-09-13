from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.




class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
                'Uses HTTP methods as function (get, post, patch , put , delete)'
                'Is similar to a traditional Django View',
                'Gives you the most control over your application logic',
                "Is mapped manually to URL's",
                ]
        return Response({'msg': "hello", 'an_apiview': an_apiview})

