# from django.shortcuts import render
# from student_app.models import student
# from django.http import JsonResponse

# def student_list(request):
#   students = student.objects.all()
#   data = {
#     'students': list(students.values())
#   }
#   return JsonResponse(data)

# def student_details(request, pk):
#   students = student.objects.get(pk=pk)
#   data = {
#     'name':student.name,
#     'age':student.age,
#     'email':student.email,
#     'phone_number':student.phone_number,
#     'address':student.address
#   }
#   return JsonResponse(data)

# # Create your views here.