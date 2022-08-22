from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.addEmployee.as_view(),name='add_url'),
    path('si/<int:pk>/',views.singleShow.as_view(),name = 'single_url'),
    path('sd/',views.ShowData.as_view(),name='showdata_url'),
    path('up/<int:pk>/',views.Upadte.as_view(),name='update_url'),
    path('dl/<int:pk>/',views.delete.as_view(),name='delete_url'),
    path('re/<int:pk>/',views.remove.as_view(),name='remove_url'),
    path('ui/<int:pk>/',views.UpdateImage.as_view(),name='updateimage_url')
]