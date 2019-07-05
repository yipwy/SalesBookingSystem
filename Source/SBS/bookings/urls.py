from django.urls import path
from .views import list_companies, create_company, update_company, delete_company, PhaseListView


urlpatterns = [

    path('', list_companies, name='list_companies'),
    path('new', create_company, name='create_companies'),
    path('update/<int:id>', update_company, name='update_company'),
    path('delete/<int:id>', update_company, name='delete_company'),
    path('phaseview/', PhaseListView.as_view(), name='phase-list'),
]
