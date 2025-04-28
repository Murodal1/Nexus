from django.urls import path, include
from .views import get_list_blog, detail_blog, BlogGenericAPIView, BlogGenericDetailAPIView, BlogGenericAPIViewMixin, BlogGenericDetailAPIViewMixin
from .views import ConcreateAPIView,ConcreateDetailAPIView, BlogViewSet, FBVAPIBlog, FBVAPIBlogDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BlogViewSet)

urlpatterns = [
    path("", get_list_blog, name='blog-list'),
    path("<int:pk>/", detail_blog, name='detail-blog'),
    path("fbv/", FBVAPIBlog.as_view()),
    path("fbv/<int:pk>/", FBVAPIBlogDetail.as_view()),
    path("generic/", BlogGenericAPIView.as_view()),
    path("generic/<int:pk>/", BlogGenericDetailAPIView.as_view()),
    path("generic/mix/", BlogGenericAPIViewMixin.as_view()),
    path("generic/mix/<int:pk>/", BlogGenericDetailAPIViewMixin.as_view()),
    path("generic/con/", ConcreateAPIView.as_view()),
    path("generic/con/<int:pk>/", ConcreateDetailAPIView.as_view()),
    path("set/", include(router.urls)),
]