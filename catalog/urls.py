from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='item'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
]