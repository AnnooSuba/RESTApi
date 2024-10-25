from student_app.models import Student
from rest_framework.response import Response
from student_app.api.serializers import StudentSerializer
from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def student_list(request):
  if request.method == 'GET':
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  
@api_view(['GET','PUT','DELETE'])

def student_details(request, pk):
  if request.method == 'GET':
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
    
  if request.method == 'DELETE':
    student = Student.objects.get(pk=pk)
    student.delete()
    return Response({'message': 'student deleted successfully'})
    
    

# Create your views here.