from typing import List
from django.core.mail import EmailMessage
from src.common.exceptions import ObjectNotFoundException


class Service:
    model = None

    @classmethod
    def get(cls, *args, **kwargs) -> model:
        try:
            return cls.model.objects.get(*args, **kwargs)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException(f'{cls.model.__name__} not found')

    @classmethod
    def filter(cls, *args, **kwargs) -> List[model]:
        return cls.model.objects.filter(*args, **kwargs)


class SendEmailService:
    @classmethod
    def my_message(cls, student):
        email_body = f"{student.full_name}, вы были добавлены в электронную систему школы '{student.grade.school.name}', в класс {student.grade.name}"
        email_subject = "Добавление в систему"
        return email_body, email_subject

    @classmethod
    def send_email(cls, student):
        email_body, email_subject  = cls.my_message(student)
        email = EmailMessage(subject=email_subject, body=email_body, to=[student.email])
        email.send()
