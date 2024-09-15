from django.urls import path
from . import views
#namespacing of url
app_name='food'
urlpatterns=[
    path('',views.IndexClassView.as_view(),name="index"),
    path('<int:pk>/',views.FoodDetail.as_view(),name="detail"),
    path('item/',views.item,name='item'),
    #add item
    path('add/',views.CreateItem.as_view(),name="add"),
    #edit /update functionality
    path('update/<int:item_id>/',views.update_item,name="update"),
    #delete
    path('delete/<int:item_id>/',views.delete_view,name="delete")
]