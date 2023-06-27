from rest_framework import serializers
from src.grades.models import Student, Grade, School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name',)


class GradeSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=False)
    class Meta:
        model = Grade
        fields = ('id', 'name', 'school')


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    grade_id = serializers.CharField(write_only=True)
    grade = GradeSerializer(many=False, required=False)

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'email', 'birth_date', 'adress',
                  'sex', 'photo', 'grade_id', 'grade')


class MailingSerializer(serializers.Serializer):
    message = serializers.CharField()
