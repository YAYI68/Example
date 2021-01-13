from django.urls import path,include
from school_app.views import *

app_name = 'school'

urlpatterns = [
    path('',School_listView.as_view(),name='list'),
    path('<pk>/',School_DetailView.as_view(),name='detail'),
    path('update/<pk>/',School_UpdateView.as_view(),name='update'),
    path('delete/<pk>/',School_DeleteView.as_view(),name='delete')
]
