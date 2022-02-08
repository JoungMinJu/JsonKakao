from django.urls import path, include
from .views import CommentViewSet, CommunityViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import urls

router = DefaultRouter()
# 첫 번쨰 인자는 url의 prefix
# 두 번째 인자는 viewSet
router.register(r'community',CommunityViewSet)
router.register(r'comment',CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# # 참고할만한 두번째 방법
#
# # 커뮤니티 목록
# community_list = CommunityViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
#
# # 커뮤니티 디테일 수정 삭제
# community_detail = CommunityViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'delete':'destroy'
# })
#
# # PK가 필요한 작업과 불필요한 작업을 나눔
#
# # 댓글
# comment_list = CommentViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
#
# comment_detail = CommentViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'delete':'destroy'
# })
#
# urlpatterns = [
#     path('community/', community_list),
#     path('community/<int:pk>/', community_detail),
#     path('comment/', comment_list),
#     path('comment/<int:pk>', comment_detail),
# ]