from django.db import models
from src.common.models import BaseModel
from src.users.models import Teacher

from django.dispatch import receiver
from django.db.models.signals import post_save

class School(BaseModel):
    name = models.CharField(max_length=350, verbose_name='Наименвоание')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'schools'
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
        ordering = ('name',)


class Grade(BaseModel):
    name = models.CharField(max_length=350, verbose_name='Наименование')
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name='grades',
                               verbose_name='Школа')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE,
                                   related_name='grade',
                                   verbose_name='Учитель')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'grades'
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ('school', 'name')

class Student(BaseModel):
    MALE = '1'
    FEMALE = '2'
    SEX_CHOISE = (
        (MALE, 'мужской'),
        (FEMALE, 'женский')
    )
    full_name = models.CharField(max_length=350, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    birth_date = models.DateField(verbose_name='Дата рождения')
    adress = models.CharField(max_length=350, verbose_name='Адрес')
    sex = models.CharField(max_length=1, choices=SEX_CHOISE,
                           verbose_name='Пол')
    photo = models.ImageField(max_length=500, null=True, blank=True,
                              upload_to="students/photo/%Y/%m/%d",
                              verbose_name='Фото ученика')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,
                              related_name='students',
                              verbose_name='Класс')
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        db_table = 'srudents'
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ('grade', 'full_name')


@receiver(post_save, sender=Student)
def call_student_api(sender, instance, **kwargs):
    print(f'Был создан новый ученик {instance}')