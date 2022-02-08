from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청이 들어오면 허용
        # safe_methods = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # request.user가 Community의 user와 동일한지 확인
        return obj.writer == request.user
