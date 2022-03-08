from django.urls import path
from.views import *

urlpatterns=[
  path('list/', categories, name='categorylist'),
  path('<int:pk>/', get_single_category, name='category'),
]