from django.contrib.auth.models import AbstractUser
from django.db import models


# Переопределил модель пользователя, чтобы поменять метод __str__
class CustomUser(AbstractUser):
    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip() if full_name.strip() else self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('first_name', 'last_name', 'date_joined')


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField('описание пользователя в профиле (биография)', blank=True)
    avatar = models.ImageField('аватар', upload_to='avatars/', blank=True)
    social_links = models.ManyToManyField(
        'SocialLink',
        related_name='user_profiles',
        blank=True,
        verbose_name='ссылки на социальные сети'
    )
    phone_number = models.CharField('номер телефона', max_length=15, blank=True)
    birthdate = models.DateField('дата рождения', null=True, blank=True)

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'
        ordering = ('user',)

    def __str__(self) -> str:
        return self.user_fio()

    def user_fio(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class SocialLink(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='профиль пользователя')
    platform_name = models.CharField('название социальной сети', max_length=255)
    link = models.URLField('ссылка')

    class Meta:
        verbose_name = 'ссылка на социальную сеть'
        verbose_name_plural = 'ссылки на социальные сети'

    def __str__(self):
        return self.user_profile.user_fio() + '      ' + self.platform_name


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
    members = models.ManyToManyField(CustomUser, through='ProjectMembership', verbose_name='участники')
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='created_projects',
        verbose_name='создатель проекта'
    )
    image = models.ImageField('изображение', upload_to='project_images/', blank=True)

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name


class ProjectMembership(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='участник')
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
        CustomUser,
        on_delete=models.CASCADE,
        related_name='assigned_tasks',
        verbose_name='ответственный'
    )
    collaborators = models.ManyToManyField(
        CustomUser,
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

    def __str__(self):
        return self.title + ' для ' + self.project.__str__()


class TaskComment(TimeStampedModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='задача')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='пользователь')
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

    def __str__(self) -> str:
        return self.user.__str__() + ': ' + self.text


class TaskMedia(TimeStampedModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='задача')
    image = models.ImageField('изображение', upload_to='task_images/', blank=True)
    file = models.FileField('файл', upload_to='task_files/', blank=True)

    class Meta:
        verbose_name = 'медиа для задачи'
        verbose_name_plural = 'медиа для задач'
