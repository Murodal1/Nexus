from django.urls import path, include
from .views import get_list_ctg, detail_ctg, CategoryView, CategoryDetailView, CategoryGenericAPIView, CategoryGenericDetailAPIView
from .views import CategoryViewSet, ConcreateAPIView, ConcreateDetailAPIView, CategoryGenericAPIViewMixin, CategoryGenericDetailAPIViewMixin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CategoryViewSet)

urlpatterns = [
    path("", get_list_ctg, name='category-list'),
    path("<int:pk>/", detail_ctg, name='detail-ctg'),
    path("cls/", CategoryView.as_view(), name='ctg-list-cls'),
    path("cls/<int:pk>/", CategoryDetailView.as_view(), name='ctg-id-cls'),
    path("generic/", CategoryGenericAPIView.as_view()),
    path("generic/<int:pk>/", CategoryGenericDetailAPIView.as_view()),
    path("gen/mix/", CategoryGenericAPIViewMixin.as_view()),
    path("gen/mix/<int:pk>/", CategoryGenericDetailAPIViewMixin.as_view()),
    path("gen/con/", ConcreateAPIView.as_view()),
    path("gen/con/<int:pk>/", ConcreateDetailAPIView.as_view()),
    path("set/", include(router.urls))
]