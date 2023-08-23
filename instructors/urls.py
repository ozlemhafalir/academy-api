from django.urls import path
from instructors import views

urlpatterns = [
    path('instructors/', views.InstructorList.as_view()),
    path('instructors/<int:pk>/', views.InstructorDetail.as_view()),
]
