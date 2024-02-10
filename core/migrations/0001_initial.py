# Generated by Django 5.0.2 on 2024-02-10 21:41

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "platform_name",
                    models.CharField(
                        max_length=255, verbose_name="название социальной сети"
                    ),
                ),
                ("link", models.URLField(verbose_name="ссылка")),
            ],
            options={
                "verbose_name": "ссылка на социальную сеть",
                "verbose_name_plural": "ссылки на социальные сети",
            },
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата обновления"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="название")),
                ("description", models.TextField(verbose_name="описание")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="project_images/",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_projects",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="создатель проекта",
                    ),
                ),
            ],
            options={
                "verbose_name": "проект",
                "verbose_name_plural": "проекты",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ProjectMembership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата обновления"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[("manager", "Manager"), ("developer", "Developer")],
                        max_length=50,
                        verbose_name="роль",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.project",
                        verbose_name="проект",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="участник",
                    ),
                ),
            ],
            options={
                "verbose_name": "участие в проекте",
                "verbose_name_plural": "участия в проектах",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="members",
            field=models.ManyToManyField(
                through="core.ProjectMembership",
                to=settings.AUTH_USER_MODEL,
                verbose_name="участники",
            ),
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата обновления"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="заголовок")),
                ("description", models.TextField(verbose_name="описание")),
                (
                    "due_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="срок выполнения"
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("low", "Low"),
                            ("medium", "Medium"),
                            ("high", "High"),
                        ],
                        max_length=255,
                        verbose_name="приоритет",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("todo", "To Do"),
                            ("in_progress", "In Progress"),
                            ("done", "Done"),
                        ],
                        max_length=255,
                        verbose_name="статус",
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_tasks",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="ответственный",
                    ),
                ),
                (
                    "collaborators",
                    models.ManyToManyField(
                        blank=True,
                        related_name="collaborating_tasks",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="дополнительные сотрудники",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.project",
                        verbose_name="проект",
                    ),
                ),
            ],
            options={
                "verbose_name": "задача",
                "verbose_name_plural": "задачи",
                "ordering": ["-due_date"],
            },
        ),
        migrations.CreateModel(
            name="TaskComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата обновления"
                    ),
                ),
                ("text", models.TextField(verbose_name="текст")),
                (
                    "parent_comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.taskcomment",
                        verbose_name="родительский комментарий",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.task",
                        verbose_name="задача",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "комментарий к задаче",
                "verbose_name_plural": "комментарии к задачам",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="TaskMedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата обновления"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="task_images/", verbose_name="изображение"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True, upload_to="task_files/", verbose_name="файл"
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.task",
                        verbose_name="задача",
                    ),
                ),
            ],
            options={
                "verbose_name": "медиа для задачи",
                "verbose_name_plural": "медиа для задач",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата обновления"
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True,
                        verbose_name="описание пользователя в профиле (биография)",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, upload_to="avatars/", verbose_name="аватар"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="номер телефона"
                    ),
                ),
                (
                    "birthdate",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата рождения"
                    ),
                ),
                (
                    "social_links",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_profiles",
                        to="core.sociallink",
                        verbose_name="ссылки на социальные сети",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "профиль пользователя",
                "verbose_name_plural": "профили пользователей",
            },
        ),
        migrations.AddField(
            model_name="sociallink",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.userprofile",
                verbose_name="профиль пользователя",
            ),
        ),
        migrations.CreateModel(
            name="AdminProfileProxy",
            fields=[],
            options={
                "verbose_name": "профиль администратора",
                "verbose_name_plural": "профили администраторов",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("core.userprofile",),
        ),
    ]
