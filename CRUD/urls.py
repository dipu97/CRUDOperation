from django.urls import path

from .import views
urlpatterns=[
    path('',views.DatasetInsertView.as_view(),name='home'),
    path('details/<int:pk>',views.IndexviewSet.as_view(),name='Index'),
]