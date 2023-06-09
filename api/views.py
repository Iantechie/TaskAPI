from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
# from django.http import JsonResponse

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update View':'/task-update/<str:pk>/',
        'Delete View':'/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    serilizer = TaskSerializer(instance=task, data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return Response(f' Task with title "{task.title}" deleted successfully!')