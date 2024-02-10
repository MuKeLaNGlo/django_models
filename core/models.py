from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('описание пользователя в профиле (биография)', blank=True)
    avatar = models.ImageField('аватар', upload_to='avatars/', blank=True)
    social_links = models.ManyToManyField('SocialLink', related_name='user_profiles', blank=True)
    phone_number = models.CharField('номер телефона', max_length=15, blank=True)
    birthdate = models.DateField('дата рождения', null=True, blank=True)

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'


class SocialLink(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='профиль пользователя')
    platform_name = models.CharField('название социальной сети', max_length=255)
    link = models.URLField('ссылка')

    class Meta:
        verbose_name = 'социальная ссылка'
        verbose_name_plural = 'социальные ссылки'


class AdminProfileProxy(UserProfile):
    class Meta:
        proxy = True
        verbose_name = 'профиль администратора'
        verbose_name_plural = 'профили администраторов'

    def grant_admin_rights(self):
        """Метод для предоставления прав администратора пользователю."""
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

    def revoke_admin_rights(self):
        """Метод для отзыва прав администратора у пользователя."""
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.save()


class Project(TimeStampedModel):
    name = models.CharField('название', max_length=255)
    description = models.TextField('описание')
    members = models.ManyToManyField(User, through='ProjectMembership', verbose_name='участники')
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_projects',
        verbose_name='создатель проекта'
    )
    image = models.ImageField('изображение', upload_to='project_images/', blank=True)

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
        ordering = ['-created_at']


class ProjectMembership(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='участник')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='проект')
    role = models.CharField('роль', max_length=50, choices=[('manager', 'Manager'), ('developer', 'Developer')])

    class Meta:
        verbose_name = 'участие в проекте'
        verbose_name_plural = 'участия в проектах'


class Task(TimeStampedModel):
    title = models.CharField('заголовок', max_length=255)
    description = models.TextField('описание')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='проект')
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_tasks',
        verbose_name='ответственный'
    )
    collaborators = models.ManyToManyField(
        User,
        related_name='collaborating_tasks',
        blank=True,
        verbose_name='дополнительные сотрудники'
    )
    due_date = models.DateTimeField('срок выполнения', null=True, blank=True)
    priority = models.CharField(
        'приоритет',
        max_length=255,
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
    )
    status = models.CharField(
        'статус',
        max_length=255,
        choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')]
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ['-due_date']


class TaskComment(TimeStampedModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='задача')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    text = models.TextField('текст')
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='родительский комментарий'
    )

    class Meta:
        verbose_name = 'комментарий к задаче'
        verbose_name_plural = 'комментарии к задачам'
        ordering = ['-created_at']


class TaskMedia(TimeStampedModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='задача')
    image = models.ImageField('изображение', upload_to='task_images/', blank=True)
    file = models.FileField('файл', upload_to='task_files/', blank=True)

    class Meta:
        verbose_name = 'медиа для задачи'
        verbose_name_plural = 'медиа для задач'
