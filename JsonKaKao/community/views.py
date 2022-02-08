from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, Comment, Like
from .serializers import CommentSerializer, CommunitySerializer, LikeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# 커뮤니티 목록, detail 보여주기, 수정하기 삭제하기
class CommunityViewSet(viewsets.ModelViewSet):
    # authentication 추가
    # 클라이언트 자신이 권한이 있는지를 서버에 알려주는 과정.
    # 인증에 성공한 경우, request.user = User // request.auth = 는 인증방식에 따라 설정됨
    # 실패한 경우 request.user = django.contrib.auth.models.AnonymousUser
    #           request.auth = None
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission 추가
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # 인증이 되지 않은 사용자는 Read만 할 수 있따.
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    # user field에 현재 user값을 전달해주기 위해 재정의
    # 즉 serializer.save() => serializer.save(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

# 댓글 목록, 디테일, 수정, 삭제
class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
