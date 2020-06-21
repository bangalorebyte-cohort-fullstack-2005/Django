from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from todo.models import Todo
from todo.api.serializers import todoSerializer

@api_view(['GET',])
def api_detail_view(request,id):

    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = todoSerializer(todo)
        return Response(serializer.data)


@api_view(['PUT',])
def api_update_view(request,id):

    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = todoSerializer(todo,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE',])
def api_delete_view(request,id):

    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = todo.delete()
        data={}
        if operation:
            data["status"]="deleted successfully"
        else:
            data["status"]="delete failed"
        return Response(data=data)

@api_view(['POST',])
def api_create_view(request):

    if request.method == 'POST':
        serializer=todoSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)