from django.contrib import admin
from src.grades.models import School, Grade, Student


class GradeInline(admin.StackedInline):
    model = Grade
    exclude = ("created_at", "updated_at")
    extra = 0

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class StudentInline(admin.StackedInline):
    model = Student
    exclude = ("created_at", "updated_at")
    extra = 0

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    list_filter = ("name",)
    ordering = ('name', "-created_at")
    exclude = ("created_at", "updated_at")
    inlines = (GradeInline,)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return School.objects.all()
        return School.objects.filter(is_deleted=False)
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name", 'school')
    list_display_links = ("name",)
    list_filter = ("name", 'school')
    ordering = ('school', 'name', "-created_at")
    exclude = ("created_at", "updated_at")
    inlines = (StudentInline,)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Grade.objects.all()
        return Grade.objects.filter(is_deleted=False)
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", 'birth_date', 'grade', 'sex')
    list_display_links = ("full_name",)
    list_filter = ("full_name", 'birth_date', 'grade', 'sex')
    ordering = ('grade', 'full_name', "birth_date")
    exclude = ("created_at", "updated_at")

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Student.objects.all()
        return Student.objects.filter(is_deleted=False)
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
