from GenericApp import views
from django.urls import path, include


urlpatterns = [
    path('data/', views.GenericView_List.as_view()),
    path('data/<int:pk>/', views.GenericView_Details.as_view()),
]
