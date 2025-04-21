from django.urls import path
from .views import get_list_prd, detail_prd

urlpatterns = [
    path("", get_list_prd, name='product-list'),
    path("<int:pk>/", detail_prd, name='detail-prd')
]