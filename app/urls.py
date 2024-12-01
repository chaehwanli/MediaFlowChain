from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),  # GET 요청으로 전체 목록 조회
    path('<int:id>/', views.media_detail, name='media_detail'),  # 특정 ID 조회
    path('create/', views.media_create, name='media_create'),  # POST 요청으로 새 데이터 생성
    path('<int:id>/update/', views.media_update, name='media_update'),  # PUT 요청으로 데이터 업데이트
    path('<int:id>/delete/', views.media_delete, name='media_delete'),  # DELETE 요청으로 데이터 삭제
]