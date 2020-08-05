from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import TaskSerializer
from .models import Task
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    overview_list={
        'List':'api/task-list',
        'Detail View':'api/task-detail/<str:pk>',
        'create':'api/task-create',
        'Update':'api/task-update/<str:pk>',
        'Delete':'api/task-delete/<str:pk>'
    }
    return Response(overview_list)

@api_view(['GET'])
def task_list(request):
    task=Task.objects.all().order_by('-id')
    serializer=TaskSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_view(request,pk):
    try:
        task=Task.objects.get(id=pk)
        serializer=TaskSerializer(task,many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response("Item Doesn't Exists",status=404)


@api_view(['POST'])
def task_create(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def task_update(request,pk):
    try:
        task=Task.objects.get(id=pk)
        serializer=TaskSerializer(instance=task,data=request.data)
        get_value=TaskSerializer(task,many=False)
        if request.method=="POST":
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        elif request.method=="GET":
            return Response(get_value.data)
    except ObjectDoesNotExist:
        return Response("Item Not Available",status=404)


# class TaskUpdate(APIView):
#     def get(self,request,pk):
#         task=Task.objects.get(id=pk)
#         serializer=TaskSerializer(task,many=False)
#         return Response(serializer.data)

#     def post(self,request,pk):
#         task=Task.objects.get(id=pk)
#         serializer=TaskSerializer(instance=task,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request,pk):
    try:
        task=Task.objects.get(id=pk)
        task.delete()
        return Response("Item Deleted Successfylly")
    except ObjectDoesNotExist:
        return Response("Item Not Found",status=404)