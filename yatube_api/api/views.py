from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)

from posts.models import Post, Group, Follow
from .serializers import (
    PostSerializer, GroupSerializer, FollowSerializer, CommentSerializer)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return self.get_post().comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
