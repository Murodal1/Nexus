from django.urls import path
from .views import get_list_ctg, detail_ctg, CategoryView, CategoryDetailView

urlpatterns = [
    path("", get_list_ctg, name='category-list'),
    path("<int:pk>/", detail_ctg, name='detail-ctg'),
    path("cls/", CategoryView.as_view(), name='ctg-list-cls'),
    path("cls/<int:pk>/", CategoryDetailView.as_view(), name='ctg-id-cls')
]