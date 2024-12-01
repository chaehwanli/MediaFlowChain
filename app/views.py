from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Movie # C:\GitHubRepo\Django\202412_prj\app\models.py

# Create your views here.


# GET 요청으로 전체 목록 조회
def media_list(request):
    if request.method == 'GET':
        media_items = Movie.objects.all().values()
        return JsonResponse(list(media_items), safe=False)

# 특정 ID 조회
def media_detail(request, id):
    if request.method == 'GET':
        media_item = get_object_or_404(Movie, id=id)
        return JsonResponse({
            'id': media_item.id,
            'name': media_item.name,
            'description': media_item.description,
        })

# POST 요청으로 새 데이터 생성
@csrf_exempt
def media_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            media_item = Movie.objects.create(
                name=data['name'],
                description=data['description']
            )
            return JsonResponse({'message': 'Media created', 'id': media_item.id}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid input data'}, status=400)

# PUT 요청으로 데이터 업데이트
@csrf_exempt
def media_update(request, id):
    if request.method == 'PUT':
        media_item = get_object_or_404(Movie, id=id)
        try:
            data = json.loads(request.body)
            media_item.name = data.get('name', media_item.name)
            media_item.description = data.get('description', media_item.description)
            media_item.save()
            return JsonResponse({'message': 'Media updated'})
        except KeyError:
            return JsonResponse({'error': 'Invalid input data'}, status=400)

# DELETE 요청으로 데이터 삭제
@csrf_exempt
def media_delete(request, id):
    if request.method == 'DELETE':
        media_item = get_object_or_404(Movie, id=id)
        media_item.delete()
        return JsonResponse({'message': 'Media deleted'})
