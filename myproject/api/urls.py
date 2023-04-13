from django.urls import path
from . import views

urlpatterns = [
    path('pessoas/', views.PessoaProfissionalListCreate.as_view(), name='pessoa_profissional_list_create'),
    path('pessoas/<int:pk>/', views.PessoaProfissionalRetrieveUpdateDestroy.as_view(), name='pessoa_profissional_retrieve_update_destroy'),
    path('consultas/', views.ConsultaListCreate.as_view(), name='consulta_list_create'),
    path('consultas/<int:pk>/', views.ConsultaRetrieveUpdateDestroy.as_view(), name='consulta_retrieve_update_destroy'),
    path('consultas/pessoa/<int:pessoa_profissional_id>/', views.ConsultasPorPessoaProfissional.as_view(), name='consultas_por_pessoa_profissional'),
]
