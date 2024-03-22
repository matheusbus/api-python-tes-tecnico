from django.urls import path

from .views import ClienteListCreateView
from .views import ClienteDetailView
from .views import AllClienteListView
from .views import ClienteUpdateView
from .views import NovoClienteAPIView


urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list'),
    path('clientes/register', NovoClienteAPIView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('cliente/all/', AllClienteListView.as_view(), name='all-clientes-list'),  
    path('cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
]