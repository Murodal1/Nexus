from django.urls import path
from .views import get_list_rgn, detail_rgn

urlpatterns = [
    path("", get_list_rgn, name='region-list'),
    path("<int:pk>/", detail_rgn, name='detail-rgn')
]