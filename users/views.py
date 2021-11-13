from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def userList(_request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getUser(_request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)

        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("User not found", status=404)


@api_view(['POST'])
def createUser(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Something went wrong", status=400)
    except Exception as e:
        print(e)
        return Response(data=e)
    #     return Response("Error when create user", status=500)
    # except Exception:
    #     return Response(f"User with email: {request.data['email']} already exist", status=400)


@api_view(['PUT'])
def updateUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return serializer.data

        return Response("Error when update user", status=500)
    except User.DoesNotExist:
        return Response("User not found", status=404)


@api_view(['DELETE'])
def deleteUser(_request, pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        return Response('User deleted')
    except User.DoesNotExist:
        return Response("User not found", status=404)
