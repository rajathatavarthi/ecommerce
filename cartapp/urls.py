from django.urls import path
from .import views
app_name='cartapp'
urlpatterns=[
    path('addcart/',views.addcart),
    path('insertcart',views.insertcart),
    path('viewcart',views.viewcart),
    path('delete/',views.delete),
    path('display',views.delete),
    path('modifycart',views.modifycart),
    path('modifiedcart',views.modifiedcart),
    path('checkout',views.checkout),
]