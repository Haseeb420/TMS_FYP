import json
from django.shortcuts import render
from TMS_API import serializers
from TMS_Models import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, viewsets

# Create your views here.

"""
Users related apis starts here
"""


# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = models.Users.objects.all()
#     serializer_class = serializers.UsersSerializer


class UsersView(APIView):
    def get(self, request, pk=None, format=None):
        try:
            if pk:
                try:
                    user = models.Users.objects.get(UserId=pk)
                    user_serializer = serializers.UsersSerializer(user)
                    return Response(user_serializer.data, status=200)
                except models.Users.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                users = models.Users.objects.all()
                user_serializer = serializers.UsersSerializer(users, many=True)
                return Response(user_serializer.data, 200)
        except Exception as e:
            msg = {'msg': 'Error occured', 'error': e}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        user_serializer = serializers.UsersSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            msg = {'msg': 'users added successfully'}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, 200)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            user = models.Users.objects.get(UserId=pk)
            user_serializer = serializers.UsersSerializer(
                user, data=request.data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                msg = {'msg': 'User updated successfully'}
                json_data = JSONRenderer().render(msg)
                return Response(json_data, 200)
        except models.Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            user = models.Users.objects.get(UserId=pk).delete()
            msg = {'msg': 'User deleted successfully'}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, status=status.HTTP_204_NO_CONTENT)
        except models.Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AccountsTypeView(viewsets.ModelViewSet):
    queryset = models.AccountsType.objects.all()
    serializer_class = serializers.AccountsTypeSerializer


class UserAuthView(APIView):
    def get(self, request, pk=None, format=None):
        try:
            if pk:
                try:
                    # get user auth by Email and  Joining Date
                    user_auth = models.UserAuth.objects.get(UserId=pk)
                    data = {
                        "UserAuthId": user_auth.UserAuthId,
                        "Email": user_auth.Email,
                        "JoinnigDate": user_auth.JoinnigDate,
                        "UserId": user_auth.UserId.UserId,
                    }
                    json_data = JSONRenderer().render(data)
                    return Response(json_data, status=200)
                except models.UserAuth.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                user_auth = models.UserAuth.objects.all()
                users = []
                for i in user_auth:
                    data = {
                        "UserAuthId": i.UserAuthId,
                        "Email": i.Email,
                        "JoinnigDate": i.JoinnigDate,
                        "UserId": i.UserId.UserId,
                    }
                    users.append(data)

                json_data = JSONRenderer().render(users)
                return Response(json_data, 200)
        except Exception as e:
            msg = {'msg': 'Error occured', 'error': e}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        user_auth_serializer = serializers.UserAuthSerializer(
            data=request.data)
        if user_auth_serializer.is_valid():
            user_auth_serializer.save()
            msg = {'msg': 'UserAuth added successfully'}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, 200)
        return Response(user_auth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            user_auth = models.UserAuth.objects.get(UserAuthId=pk)
            user_auth_serializer = serializers.UserAuthSerializer(
                user_auth, data=request.data, partial=True)
            if user_auth_serializer.is_valid():
                user_auth_serializer.save()
                msg = {'msg': 'UserAuth updated successfully'}
                json_data = JSONRenderer().render(msg)
                return Response(json_data, 200)
        except models.UserAuth.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(user_auth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            user_auth = models.UserAuth.objects.get(UserAuthId=pk).delete()
            msg = {'msg': 'UserAuth deleted successfully'}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, status=status.HTTP_204_NO_CONTENT)
        except models.UserAuth.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


"""
Users related apis ends here
"""

"""
Packages related apis starts here
"""


class PackageTypeView(viewsets.ModelViewSet):
    queryset = models.Packages.objects.all()
    serializer_class = serializers.PackagesSerializer


class PackageView(APIView):
    def get(self, request, pk=None, format=None):
        try:
            if pk:
                try:
                    package = models.Package.objects.get(PackageId=pk)
                    package_serializer = serializers.PackagesSerializer(
                        package)
                    return Response(package_serializer.data, status=200)
                except models.Package.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                package = models.Package.objects.all()
                package_serializer = serializers.PackagesSerializer(
                    package, many=True)
                return Response(package_serializer.data, 200)
        except Exception as e:
            msg = {'msg': 'Error occured', 'error': e}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        package_serializer = serializers.PackagesSerializer(
            data=request.data)
        if package_serializer.is_valid():
            package_serializer.save()
            msg = {'msg': 'Package added successfully'}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, 200)
        return Response(package_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            package = models.Package.objects.get(PackageId=pk)
            package_serializer = serializers.PackagesSerializer(
                package, data=request.data, partial=True)
            if package_serializer.is_valid():
                package_serializer.save()
                msg = {'msg': 'Package updated successfully'}
                json_data = JSONRenderer().render(msg)
                return Response(json_data, 200)
        except models.Package.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            package = models.Package.objects.get(PackageId=pk).delete()
            msg = {'msg': 'Package deleted successfully'}
            json_data = JSONRenderer().render(msg)
            return Response(json_data, status=status.HTTP_204_NO_CONTENT)
        except models.Package.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


"""
packages related api ends here
"""
