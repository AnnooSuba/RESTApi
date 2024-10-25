from rest_framework import serializers
from student_app.models import Student

# modelserializer concept
# we dont want to write all fields..whatever there in model field this modelField map that accordingly...

class StudentSerializer(serializers. ModelSerializer):
  class Meta:
    model = Student
    # fields = "__all__"
    # fields = ['id', 'name', 'email', 'phone_number', 'address']
    exclude = ['name']
    
def validate(self, data):
  if data['name'] == data['description']:
    raise serializers.ValidationError("Title and Description should be different!")
  else:
    return data
  
def validate_name(self, value):
  if len(value) < 2:
    raise serializers.ValidationError("Name is too short!")
  else:
    return value


# def name_length(value):
#   if len(value) < 2:
#     raise serializers.ValidationError("Name is too short!") 

# class StudentSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators = [name_length])
#   age = serializers.IntegerField()
#   email = serializers.EmailField()
#   phone_number = serializers.IntegerField()
#   address = serializers.CharField()
  
#   def create(self, validated_data):
#     return Student.objects.create(**validated_data)
  
#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.age = validated_data.get('age', instance.age)
#     instance.email = validated_data.get('email', instance.email)
#     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
#     instance.address = validated_data.get('address', instance.address)
#     instance.save()
#     return instance
  
#   def validate(self, data):
#     if data['name'] ==  data['address']:
#       raise serializers. ValidationError("Title and Description should be different!")
#     else:
#       return data
  
  
  # def validate_name(self, value):
  #   if len(value) < 2:
  #     raise serializers. ValidationError("Name is too short!")
  #   else:
  #     return value
  
  
  
  