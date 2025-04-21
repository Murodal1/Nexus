from django.urls import path
from .views import get_list_ctg, detail_ctg

urlpatterns = [
    path("", get_list_ctg, name='category-list'),
    path("<int:pk>/", detail_ctg, name='detail-ctg')
]