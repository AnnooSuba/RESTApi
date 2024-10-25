
from django.urls import path, include
from student_app.api.views import student_list, student_details

urlpatterns = [
    path('list/', student_list, name='student-list' ),
    path('<int:pk>/', student_details, name = 'student-details')
]