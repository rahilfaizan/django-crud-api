# from django.shortcuts import render
# from django.http import JsonResponse
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import TaskSerializer
#
# from .models import Task
# # Create your views here.
#
# @api_view(['GET'])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/task-list/',
# 		'Detail View':'/task-detail/<str:pk>/',
# 		'Create':'/task-create/',
# 		'Update':'/task-update/<str:pk>/',
# 		'Delete':'/task-delete/<str:pk>/',
# 		}
#
# 	return Response(api_urls)
#
# @api_view(['GET'])
# def taskList(request):
# 	tasks = Task.objects.all().order_by('-id')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = TaskSerializer(data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Task.objects.get(id=pk)
# 	task.delete()
#
# 	return Response('Item succsesfully delete!')
#
#
#
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .serializers import BroSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .models import Task
from .models import Bro
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	bros = Bro.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	bro_serializer = BroSerializer(bros, many=True)
	result_serializer = serializer.data + bro_serializer.data
	return Response(result_serializer)


@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	bros = Bro.objects.get(id=pk)
	bro_serializer = BroSerializer(bros, many=False)
	result_serializer = serializer.data + bro_serializer.data
	return Response(result_serializer)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	bro_serializer = BroSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	if bro_serializer.is_valid():
		bro_serializer.save()

	result_serializer = serializer.data + bro_serializer.data
	return Response(result_serializer)


@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)
	bro = Bro.objects.get(id=pk)
	bro_serializer = BroSerializer(instance=bro, data=request.data)
	if serializer.is_valid() and bro_serializer.is_valid():
		serializer.save()
		bro_serializer.save()

	result_serializer = serializer.data + bro_serializer.data
	return Response(result_serializer)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



