from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.users.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    list_display = ("phone_number", "subject", "is_active",
                   "is_staff", "is_superuser", "is_deleted")
    list_display_links = ("phone_number",)
    list_filter = ("phone_number", "subject", "is_active",
                   "is_staff", "is_superuser", "is_deleted")
    list_editable = ("is_active", "is_staff")
    readonly_fields = ("created_at", "updated_at", "last_login")
    search_fields = ("username",)
    ordering = ('-created_at',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Teacher.objects.all()
        return Teacher.objects.filter(is_deleted=False)
    
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
