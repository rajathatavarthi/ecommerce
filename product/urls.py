from django.urls import path
from .import views
app_name='product'
urlpatterns=[
    path('search/',views.search),
    path('searchh/',views.searchh),
]