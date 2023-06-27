from src.common.services import Service, SendEmailService
from src.grades.models import Student, Grade


class GradeService(Service):
    model = Grade


class StudentService(Service):
    model = Student

    @classmethod
    def create(cls, data):
        grade = GradeService.get(id=data.get('grade_id'))
        student = cls.model.objects.create(
            full_name=data.get('full_name'),
            email=data.get('email'),
            birth_date=data.get('birth_date'),
            adress=data.get('adress'),
            sex=data.get('sex'),
            photo=data.get('photo'),
            grade=grade
        )
        SendEmailService.send_email(student)