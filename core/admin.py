from django.contrib import admin
from django.utils.html import mark_safe

from core import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = models.CustomUser
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')


class SocialLinkInline(admin.TabularInline):
    model = models.SocialLink
    extra = 1


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'get_image')
    exclude = ('social_links',)

    def get_image(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" style="max-width: 60px; max-height: 60px; object-fit: cover;"  />'
            )
        return

    get_image.short_description = 'Аватарка'

    inlines = [SocialLinkInline]


@admin.register(models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'platform_name', 'link')


# @admin.register(models.AdminProfileProxy)
# class AdminProfileProxyAdmin(admin.ModelAdmin):
#     list_display = ('user', 'created_at', 'updated_at')

#     def get_queryset(self, request):
#         return super().get_queryset(request).filter(user__is_superuser=True)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'creator', 'created_at', 'updated_at')


@admin.register(models.ProjectMembership)
class ProjectMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'role', 'created_at', 'updated_at')


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'due_date', 'priority', 'status', 'created_at', 'updated_at')


@admin.register(models.TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'text', 'short_parent_comment', 'created_at')

    def short_parent_comment(self, obj):
        if len(str(obj.parent_comment)) > 40:
            return str(obj.parent_comment)[:37] + '...'  # Обрезаем текст до 40 символов
        elif obj.parent_comment:
            return obj.parent_comment
        return

    short_parent_comment.short_description = 'Родительский комментарий'


@admin.register(models.TaskMedia)
class TaskMediaAdmin(admin.ModelAdmin):
    list_display = ('task', 'image', 'file', 'created_at')
