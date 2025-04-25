from django.urls import path
from .views import get_list_blog, detail_blog, BlogGenericAPIView, BlogGenericDetailAPIView, BlogGenericAPIViewMixin, BlogGenericDetailAPIViewMixin

urlpatterns = [
    path("", get_list_blog, name='blog-list'),
    path("<int:pk>/", detail_blog, name='detail-blog'),
    path("generic/", BlogGenericAPIView.as_view()),
    path("generic/<int:pk>/", BlogGenericDetailAPIView.as_view()),
    path("generic/mix/", BlogGenericAPIViewMixin.as_view()),
    path("generic/mix/<int:pk>/", BlogGenericDetailAPIViewMixin.as_view()),
]