from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
# Create your views here.



class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
                'Uses HTTP methods as function (get, post, patch , put , delete)'
                'Is similar to a traditional Django View',
                'Gives you the most control over your application logic',
                "Is mapped manually to URL's",
                ]
        return Response({'msg': "hello", 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = "Hello {}".format(name)
            return Response({'message:': message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

    #pk = primary key
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': "PATCH"})


    def delete(self, request, pk=None):
        "Delete an object"
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """return a hello message"""
        a_viewset = [
                "Uses actions (list, creat, retrive, update, partial_update)",
                "Automatically maps to URLS using routers",
                "Provides more functionallity with less code",
                ]
        return Response({"message": "Hello!", "a_viewset": a_viewset })

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = "hello {}".format(name)
            return Response({"message": message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )


    # 1 woudl be the pk
    # http://localhost:8000/api/hello-viewset/1/
    def retrieve(self, request, pk=None):
         """Handle getting an object by its id"""
         return Response({"http_method":"GET"})

    # type some in that name field while being on pk=1
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_method":"PUT"})


    # click on raw data and press patch
    def partial_update(self,request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method":"PATCH"})
    # can delete the object with pk=1 above

    def destroy(self, request, pk=None):
        """Handles removing an object"""
        return Response({"http_method":"DELETE"})




class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
