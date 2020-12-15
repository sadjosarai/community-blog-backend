from django.db.models import Q
from .models import Post, Category, Tag, Formation, Lecon
from utils.permissions import (
        IsOwnerOrReadOnly, 
        IsPublish, 
        FormationHasPublish,
        IsNotPublish,
        IsAdminFormation
    )
from utils.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .serializers import (  
    LeconDetailSerializer,
    LeconCreateSerializer,

    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
    PostCreateSerializer,

    CategoryListSerializer,
    CategoryDetailSerializer,

    TagListSerializer,
    TagDetailSerializer,
    TagCreateUpdateSerializer,

    FormationListSerializer,
    FormationDetailSerializer,
    FormationCreateUpdateSerializer,
    FormationCreateSerializer,
)

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    permission_classes = [IsPublish]

class PostUpdateView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

class PostListView(ListAPIView):
    serializer_class = PostDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'body', 'description', 'user__username', 'tag__title', 'category__title']
    pagination_class = PostPageNumberPagination

    # how to use search or q
    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.filter(status="published").order_by('publish_at')
        query = self.request.GET.get("q")
        if query :
            queryset_list = queryset_list.filter(
                Q(title__icontains=q)|
                Q(body__icontains=q)|
                Q(description__icontains=q)|
                Q(user__username__icontains=q)|
                Q(tag__title__icontains=q)|
                Q(category__title__icontains=q)
            ).distinct()
        return queryset_list

class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

class TagListView(ListAPIView):
    serializer_class = TagListSerializer
    queryset = Tag.objects.all()

class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

class TagDeleteView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    lookup_field = 'title'
    lookup_url_kwarg = 'title'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

class TagUpdateView(RetrieveUpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateUpdateSerializer
    lookup_field = 'title'
    lookup_url_kwarg = 'title'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class TagCreateView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FormationCreateView(CreateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FormationDetailView(RetrieveAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    permission_classes = [IsPublish]

class FormationUpdateView(RetrieveUpdateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationCreateUpdateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class FormationDeleteView(DestroyAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

class FormationListView(ListAPIView):
    serializer_class = FormationDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'body', 'description', 'user__username', 'tag__title', 'category__title']
    pagination_class = PostPageNumberPagination

    # how to use search or q
    def get_queryset(self, *args, **kwargs):
        queryset_list = Formation.objects.filter(status="published").order_by('publish_at')
        query = self.request.GET.get("q")
        if query :
            queryset_list = queryset_list.filter(
                Q(title__icontains=q)|
                Q(body__icontains=q)|
                Q(description__icontains=q)|
                Q(user__username__icontains=q)|
                Q(tag__title__icontains=q)|
                Q(category__title__icontains=q)
            ).distinct()
        return queryset_list

class FormationCreateView(CreateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LeconDetailView(RetrieveAPIView):
    queryset = Lecon.objects.all()
    serializer_class = LeconDetailSerializer
    permission_classes = [FormationHasPublish]

class LeconUpdateView(RetrieveUpdateAPIView):
    queryset = Lecon.objects.all()
    serializer_class = LeconDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsAdminFormation]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class LeconDeleteView(DestroyAPIView):
    queryset = Lecon.objects.all()
    serializer_class = LeconDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsAdminFormation, IsNotPublish]

class LeconCreateView(CreateAPIView):
    queryset = Lecon.objects.all()
    serializer_class = LeconCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsAdminFormation, IsNotPublish]
